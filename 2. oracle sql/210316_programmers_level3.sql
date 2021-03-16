--1. 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID 순으로 조회하는 SQL문을 작성해주세요.
select a.animal_id, a.name
from animal_outs a
where not exists (select 1
                  from animal_ins b
                  where a.animal_id  = b.animal_id)
order by 1;

--2.관리자의 실수로 일부 동물의 입양일이 잘못 입력되었습니다.보호 시작일보다 입양일이 더 빠른 동물의 아이디와 이름을 조회하는 SQL문을 작성해주세요.
--  이때 결과는 보호 시작일이 빠른 순으로 조회해야합니다.
SELECT a.animal_id,a.name
from animal_ins a
where a.datetime > (select b.datetime
                    from  animal_outs b
                    where a.animal_id = b.animal_id)
order by a.datetime

--3아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요.
-- 이때 결과는 보호 시작일 순으로 조회해야 합니다.
select name, datetime
from (SELECT a.*
        from animal_ins a
        where not exists(select 1
                         from animal_outs b
                         where a.animal_id = b.animal_id)
     order by a.datetime)
where rownum <=3
/*상기 코드와 같으나, mssql의 limit 대신 fetch first 3 rows only를 사용하여 상위 3개 인덱스만 보이게 함*/
select a.name, a.datetime
from animal_ins a
where not exists(select 1
                from animal_outs b
                where a.animal_id = b.animal_id)
order by 2
fetch first 3 rows only;

--4. 입양을 간 동물 중, 보호 기간이 가장 길었던 동물 두 마리의 아이디와 이름을 조회하는 SQL문을 작성해주세요.
-- 이때 결과는 보호 기간이 긴 순으로 조회해야 합니다.
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