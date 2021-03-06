--1. 동물 보호소에 가장 먼저 들어온 동물은 언제 들어왔는지 조회하는 SQL 문을 작성해주세요.
SELECT datetime
from(
    select *
    from ANIMAL_INS
    order by datetime
    )
where rownum = 1

--2. 동물 보호소에 동물이 몇 마리 들어왔는지 조회하는 SQL 문을 작성해주세요.
SELECT count(animal_id)
from ANIMAL_INS

--3. 동물 보호소에 들어온 동물의 이름은 몇 개인지 조회하는 SQL 문을 작성해주세요. 이때 이름이 NULL인 경우는 집계하지 않으며 중복되는 이름은 하나로 칩니다.
SELECT count(distinct name)
from ANIMAL_INS
where name is not null

--4. 동물 보호소에 들어온 동물 중 고양이와 개가 각각 몇 마리인지 조회하는 SQL문을 작성해주세요. 이때 고양이를 개보다 먼저 조회해주세요.
select animal_type, count(animal_id)
from animal_ins
where regexp_like(initcap(animal_type),'Cat|Dog')
group by animal_type
order by 1;

--5. 동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회하는 SQL문을 작성해주세요. 이때 결과는 이름이 없는 동물은 집계에서 제외하며, 결과는 이름 순으로 조회해주세요.
select name, count(name) as count
from animal_ins
where name is not null
group by name
having count>1
order by name;

--6. 보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.
select to_char(datetime, 'hh24') hours, count(to_char(datetime, 'hh24')) count
from animal_outs
where to_number(to_char(datetime, 'hh24')) between 9 and 20
group by to_char(datetime, 'hh24')
order by hours
