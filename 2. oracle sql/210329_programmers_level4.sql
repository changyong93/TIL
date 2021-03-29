/*데이터 분석 팀에서는 우유(Milk)와 요거트(Yogurt)를 동시에 구입한 장바구니가 있는지 알아보려 합니다.
우유와 요거트를 동시에 구입한 장바구니의 아이디를 조회하는 SQL 문을 작성해주세요. 이때 결과는 장바구니의 아이디 순으로 나와야 합니다.*/
-- 내부 조인
select a.cart_id
from (SELECT *
      from cart_products
      where lower(name) = 'milk') a
     ,(select *
      from cart_products
      where lower(name) = 'yogurt') b
where a.cart_id = b.cart_id
order by a.cart_id;

--groupby 사용
select cart_id
from cart_products
where regexp_like (lower(name), 'milk|yogurt')
group by cart_id
having count(distinct name) = 2
order by cart_id

/*보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다.
0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요.
이때 결과는 시간대 순으로 정렬해야 합니다.*/
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

/*보호소에서 중성화 수술을 거친 동물 정보를 알아보려 합니다. 보호소에 들어올 당시에는 중성화1되지 않았지만,
보호소를 나갈 당시에는 중성화된 동물의 아이디와 생물 종, 이름을 조회하는 아이디 순으로 조회하는 SQL 문을 작성해주세요.*/
SELECT a.animal_id, a.animal_type, a.name
from ANIMAL_INS a, animal_outs b
where 1=1
and a.animal_id = b.animal_id
and not regexp_like(lower(a.sex_upon_intake), 'neutered|spayed')
and regexp_like(lower(b.sex_upon_outcome), 'neutered|spayed')