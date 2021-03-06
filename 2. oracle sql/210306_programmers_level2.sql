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

--5. ���� ��ȣ�ҿ� ���� ���� �̸� �� �� �� �̻� ���� �̸��� �ش� �̸��� ���� Ƚ���� ��ȸ�ϴ� SQL���� �ۼ����ּ���. �̶� ����� �̸��� ���� ������ ���迡�� �����ϸ�, ����� �̸� ������ ��ȸ���ּ���.
select name, count(name) as count
from animal_ins
where name is not null
group by name
having count>1
order by name;

--6. ��ȣ�ҿ����� �� �ÿ� �Ծ��� ���� Ȱ���ϰ� �Ͼ���� �˾ƺ��� �մϴ�. 09:00���� 19:59����, �� �ð��뺰�� �Ծ��� �� ���̳� �߻��ߴ��� ��ȸ�ϴ� SQL���� �ۼ����ּ���. �̶� ����� �ð��� ������ �����ؾ� �մϴ�.
select to_char(datetime, 'hh24') hours, count(to_char(datetime, 'hh24')) count
from animal_outs
where to_number(to_char(datetime, 'hh24')) between 9 and 20
group by to_char(datetime, 'hh24')
order by hours
