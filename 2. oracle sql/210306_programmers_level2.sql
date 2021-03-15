--1. ���� ��ȣ�ҿ� ���� ���� ���� ������ ���� ���Դ��� ��ȸ�ϴ� SQL ���� �ۼ����ּ���.
SELECT datetime
from(
    select *
    from ANIMAL_INS
    order by datetime
    )
where rownum = 1

--2. ���� ��ȣ�ҿ� ������ �� ���� ���Դ��� ��ȸ�ϴ� SQL ���� �ۼ����ּ���.
SELECT count(animal_id)
from ANIMAL_INS

--3. ���� ��ȣ�ҿ� ���� ������ �̸��� �� ������ ��ȸ�ϴ� SQL ���� �ۼ����ּ���. �̶� �̸��� NULL�� ���� �������� ������ �ߺ��Ǵ� �̸��� �ϳ��� Ĩ�ϴ�.
SELECT count(distinct name)
from ANIMAL_INS
where name is not null

--4. ���� ��ȣ�ҿ� ���� ���� �� ����̿� ���� ���� �� �������� ��ȸ�ϴ� SQL���� �ۼ����ּ���. �̶� ����̸� ������ ���� ��ȸ���ּ���.
select animal_type, count(animal_id)
from animal_ins
where regexp_like(initcap(animal_type),'Cat|Dog')
group by animal_type
order by 1;

--5. ���� ��ȣ�ҿ� ���� ���� �̸� �� �� �� �̻� ���� �̸��� �ش� �̸��� ���� Ƚ���� ��ȸ�ϴ� SQL���� �ۼ����ּ���.
--�̶� ����� �̸��� ���� ������ ���迡�� �����ϸ�, ����� �̸� ������ ��ȸ���ּ���.
select name, count(name) as count
from animal_ins
where name is not null
group by name
having count>1
order by name;

--6. ��ȣ�ҿ����� �� �ÿ� �Ծ��� ���� Ȱ���ϰ� �Ͼ���� �˾ƺ��� �մϴ�. 09:00���� 19:59����, �� �ð��뺰�� �Ծ��� �� ���̳� �߻��ߴ��� ��ȸ�ϴ� SQL���� �ۼ����ּ���.
--�̶� ����� �ð��� ������ �����ؾ� �մϴ�.
select to_char(datetime, 'hh24') hours, count(to_char(datetime, 'hh24')) count
from animal_outs
where to_number(to_char(datetime, 'hh24')) between 9 and 20
group by to_char(datetime, 'hh24')
order by hours

--7���� ��ȣ�ҿ� ���� ���� �� �̸��� Lucy, Ella, Pickle, Rogan, Sabrina, Mitty�� ������ ���̵�� �̸�, ���� �� �߼�ȭ ���θ� ��ȸ�ϴ� SQL ���� �ۼ����ּ���.
SELECT animal_id,name,SEX_UPON_INTAKE
from animal_ins
where regexp_like(name, 'Lucy|Ella|Pickle|Rogan|Sabrina|Mitty')
order by 1;

--8��ȣ�ҿ� ���ư��� �ҸӴϰ� �⸣�� ���� ã�� ����� ã�ƿԽ��ϴ�. �� ����� ���ϱ� �ҸӴϰ� �⸣�� ���� �̸��� 'el'�� ���ٰ� �մϴ�.
--���� ��ȣ�ҿ� ���� ���� �̸� ��, �̸��� "EL"�� ���� ���� ���̵�� �̸��� ��ȸ�ϴ� SQL���� �ۼ����ּ���. �̶� ����� �̸� ������ ��ȸ���ּ���.
--��, �̸��� ��ҹ��ڴ� �������� �ʽ��ϴ�.
SELECT animal_id, name
from animal_ins
where 1=1
and regexp_like(lower(name),'el')
and lower(animal_type) = 'dog'
order by 2;

--9��ȣ���� ������ �߼�ȭ�Ǿ����� �ƴ��� �ľ��Ϸ� �մϴ�. �߼�ȭ�� ������ SEX_UPON_INTAKE �÷��� 'Neutered' �Ǵ� 'Spayed'��� �ܾ ����ֽ��ϴ�. 
--������ ���̵�� �̸�, �߼�ȭ ���θ� ���̵� ������ ��ȸ�ϴ� SQL���� �ۼ����ּ���. �̶� �߼�ȭ�� �Ǿ��ִٸ� 'O', �ƴ϶�� 'X'��� ǥ�����ּ���.
SELECT animal_id, name
      ,case when regexp_like(sex_upon_intake,'Neutered|Spayed') then 'O'
            else 'X'
        end �߼�ȭ
from animal_ins
where 1=1
order by 1;

--10ANIMAL_OUTS ���̺��� ���� ��ȣ�ҿ��� �Ծ� ���� ������ ������ ���� ���̺��Դϴ�. ANIMAL_OUTS ���̺� ������ ������ ������, ANIMAL_ID, ANIMAL_TYPE,
--DATETIME, NAME, SEX_UPON_OUTCOME�� ���� ������ ���̵�, ���� ��, �Ծ���, �̸�, ���� �� �߼�ȭ ���θ� ��Ÿ���ϴ�.
--ANIMAL_OUTS ���̺��� ANIMAL_ID�� ANIMAL_INS�� ANIMAL_ID�� �ܷ� Ű�Դϴ�.
select *
from(SELECT a.animal_id,a.name
    from ANIMAL_OUTS a
    left join animal_ins b
    on a.animal_id = b.animal_id
    where b.animal_type is not null
    order by (b.datetime-a.datetime))
where rownum <=2

--ANIMAL_INS ���̺� ��ϵ� ��� ���ڵ忡 ����, �� ������ ���̵�� �̸�, ���� ��¥1�� ��ȸ�ϴ� SQL���� �ۼ����ּ���.
--�̶� ����� ���̵� ������ ��ȸ�ؾ� �մϴ�.
SELECT animal_id, name, to_char(datetime, 'yyyy-mm-dd')
from animal_ins
order by 1;