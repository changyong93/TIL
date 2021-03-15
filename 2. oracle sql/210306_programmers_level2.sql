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

--5. 동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회하는 SQL문을 작성해주세요.
--이때 결과는 이름이 없는 동물은 집계에서 제외하며, 결과는 이름 순으로 조회해주세요.
select name, count(name) as count
from animal_ins
where name is not null
group by name
having count>1
order by name;

--6. 보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요.
--이때 결과는 시간대 순으로 정렬해야 합니다.
select to_char(datetime, 'hh24') hours, count(to_char(datetime, 'hh24')) count
from animal_outs
where to_number(to_char(datetime, 'hh24')) between 9 and 20
group by to_char(datetime, 'hh24')
order by hours

--7동물 보호소에 들어온 동물 중 이름이 Lucy, Ella, Pickle, Rogan, Sabrina, Mitty인 동물의 아이디와 이름, 성별 및 중성화 여부를 조회하는 SQL 문을 작성해주세요.
SELECT animal_id,name,SEX_UPON_INTAKE
from animal_ins
where regexp_like(name, 'Lucy|Ella|Pickle|Rogan|Sabrina|Mitty')
order by 1;

--8보호소에 돌아가신 할머니가 기르던 개를 찾는 사람이 찾아왔습니다. 이 사람이 말하길 할머니가 기르던 개는 이름에 'el'이 들어간다고 합니다.
--동물 보호소에 들어온 동물 이름 중, 이름에 "EL"이 들어가는 개의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 이때 결과는 이름 순으로 조회해주세요.
--단, 이름의 대소문자는 구분하지 않습니다.
SELECT animal_id, name
from animal_ins
where 1=1
and regexp_like(lower(name),'el')
and lower(animal_type) = 'dog'
order by 2;

--9보호소의 동물이 중성화되었는지 아닌지 파악하려 합니다. 중성화된 동물은 SEX_UPON_INTAKE 컬럼에 'Neutered' 또는 'Spayed'라는 단어가 들어있습니다. 
--동물의 아이디와 이름, 중성화 여부를 아이디 순으로 조회하는 SQL문을 작성해주세요. 이때 중성화가 되어있다면 'O', 아니라면 'X'라고 표시해주세요.
SELECT animal_id, name
      ,case when regexp_like(sex_upon_intake,'Neutered|Spayed') then 'O'
            else 'X'
        end 중성화
from animal_ins
where 1=1
order by 1;

--10ANIMAL_OUTS 테이블은 동물 보호소에서 입양 보낸 동물의 정보를 담은 테이블입니다. ANIMAL_OUTS 테이블 구조는 다음과 같으며, ANIMAL_ID, ANIMAL_TYPE,
--DATETIME, NAME, SEX_UPON_OUTCOME는 각각 동물의 아이디, 생물 종, 입양일, 이름, 성별 및 중성화 여부를 나타냅니다.
--ANIMAL_OUTS 테이블의 ANIMAL_ID는 ANIMAL_INS의 ANIMAL_ID의 외래 키입니다.
select *
from(SELECT a.animal_id,a.name
    from ANIMAL_OUTS a
    left join animal_ins b
    on a.animal_id = b.animal_id
    where b.animal_type is not null
    order by (b.datetime-a.datetime))
where rownum <=2

--ANIMAL_INS 테이블에 등록된 모든 레코드에 대해, 각 동물의 아이디와 이름, 들어온 날짜1를 조회하는 SQL문을 작성해주세요.
--이때 결과는 아이디 순으로 조회해야 합니다.
SELECT animal_id, name, to_char(datetime, 'yyyy-mm-dd')
from animal_ins
order by 1;