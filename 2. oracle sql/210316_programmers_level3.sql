--1. �Ծ��� �� ����� �ִµ�, ��ȣ�ҿ� ���� ����� ���� ������ ID�� �̸��� ID ������ ��ȸ�ϴ� SQL���� �ۼ����ּ���.
select a.animal_id, a.name
from animal_outs a
where not exists (select 1
                  from animal_ins b
                  where a.animal_id  = b.animal_id)
order by 1;

--2.�������� �Ǽ��� �Ϻ� ������ �Ծ����� �߸� �ԷµǾ����ϴ�.��ȣ �����Ϻ��� �Ծ����� �� ���� ������ ���̵�� �̸��� ��ȸ�ϴ� SQL���� �ۼ����ּ���.
--  �̶� ����� ��ȣ �������� ���� ������ ��ȸ�ؾ��մϴ�.
SELECT a.animal_id,a.name
from animal_ins a
where a.datetime > (select b.datetime
                    from  animal_outs b
                    where a.animal_id = b.animal_id)
order by a.datetime

--3���� �Ծ��� �� �� ���� ��, ���� ���� ��ȣ�ҿ� �־��� ���� 3������ �̸��� ��ȣ �������� ��ȸ�ϴ� SQL���� �ۼ����ּ���.
-- �̶� ����� ��ȣ ������ ������ ��ȸ�ؾ� �մϴ�.
select name, datetime
from (SELECT a.*
        from animal_ins a
        where not exists(select 1
                         from animal_outs b
                         where a.animal_id = b.animal_id)
     order by a.datetime)
where rownum <=3
/*��� �ڵ�� ������, mssql�� limit ��� fetch first 3 rows only�� ����Ͽ� ���� 3�� �ε����� ���̰� ��*/
select a.name, a.datetime
from animal_ins a
where not exists(select 1
                from animal_outs b
                where a.animal_id = b.animal_id)
order by 2
fetch first 3 rows only;

--4. �Ծ��� �� ���� ��, ��ȣ �Ⱓ�� ���� ����� ���� �� ������ ���̵�� �̸��� ��ȸ�ϴ� SQL���� �ۼ����ּ���.
-- �̶� ����� ��ȣ �Ⱓ�� �� ������ ��ȸ�ؾ� �մϴ�.
select a.animal_id, a.name
from animal_outs a
left join animal_ins b
on a.animal_id = b.animal_id
order by (b.datetime - a.datetime)
fetch first 2 rows only

select *
from(SELECT a.animal_id,a.name
    from ANIMAL_OUTS a
    left join animal_ins b
    on a.animal_id = b.animal_id
    where b.animal_type is not null
    order by (b.datetime-a.datetime))
where rownum <=2