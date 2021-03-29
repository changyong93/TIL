/*������ �м� �������� ����(Milk)�� ���Ʈ(Yogurt)�� ���ÿ� ������ ��ٱ��ϰ� �ִ��� �˾ƺ��� �մϴ�.
������ ���Ʈ�� ���ÿ� ������ ��ٱ����� ���̵� ��ȸ�ϴ� SQL ���� �ۼ����ּ���. �̶� ����� ��ٱ����� ���̵� ������ ���;� �մϴ�.*/
-- ���� ����
select a.cart_id
from (SELECT *
      from cart_products
      where lower(name) = 'milk') a
     ,(select *
      from cart_products
      where lower(name) = 'yogurt') b
where a.cart_id = b.cart_id
order by a.cart_id;

--groupby ���
select cart_id
from cart_products
where regexp_like (lower(name), 'milk|yogurt')
group by cart_id
having count(distinct name) = 2
order by cart_id

/*��ȣ�ҿ����� �� �ÿ� �Ծ��� ���� Ȱ���ϰ� �Ͼ���� �˾ƺ��� �մϴ�.
0�ú��� 23�ñ���, �� �ð��뺰�� �Ծ��� �� ���̳� �߻��ߴ��� ��ȸ�ϴ� SQL���� �ۼ����ּ���.
�̶� ����� �ð��� ������ �����ؾ� �մϴ�.*/
select a.hour,
       case when b.count is null then 0
       else b.count
       end as count
from(select level-1 hour
     from dual
     connect by level <=24) a,
    (select to_number(to_char(datetime, 'hh24')) hour, count(*) count
     from animal_outs
     group by to_number(to_char(datetime, 'hh24'))) b
where a.hour = b.hour(+)
order by a.hour

select b.hour,
       case when a.count is null then 0
       else a.count
       end count
from(select to_number(to_char(datetime, 'hh24')) hour, count(*) count
     from animal_outs
     group by to_number(to_char(datetime, 'hh24'))) a
right outer join(select level-1 hour
                 from dual
                 connect by level <=24) b
on a.hour = b.hour
order by 1

/*��ȣ�ҿ��� �߼�ȭ ������ ��ģ ���� ������ �˾ƺ��� �մϴ�. ��ȣ�ҿ� ���� ��ÿ��� �߼�ȭ1���� �ʾ�����,
��ȣ�Ҹ� ���� ��ÿ��� �߼�ȭ�� ������ ���̵�� ���� ��, �̸��� ��ȸ�ϴ� ���̵� ������ ��ȸ�ϴ� SQL ���� �ۼ����ּ���.*/
SELECT a.animal_id, a.animal_type, a.name
from ANIMAL_INS a, animal_outs b
where 1=1
and a.animal_id = b.animal_id
and not regexp_like(lower(a.sex_upon_intake), 'neutered|spayed')
and regexp_like(lower(b.sex_upon_outcome), 'neutered|spayed')