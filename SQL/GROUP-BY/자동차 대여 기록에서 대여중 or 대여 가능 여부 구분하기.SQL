-- 문제 설명
-- 다음은 어느 자동차 대여 회사의 자동차 대여 기록 정보를 담은 CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블입니다. 
-- CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블은 아래와 같은 구조로 되어있으며, 
-- HISTORY_ID, CAR_ID, START_DATE, END_DATE 는 
-- 각각 자동차 대여 기록 ID, 자동차 ID, 대여 시작일, 대여 종료일을 나타냅니다.

-- Column name	Type	Nullable
-- HISTORY_ID	INTEGER	FALSE
-- CAR_ID	INTEGER	FALSE
-- START_DATE	DATE	FALSE
-- END_DATE	DATE	FALSE

-- 문제
-- CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블에서 
-- 2022년 10월 16일에 대여 중인 자동차인 경우 '대여중' 이라고 표시하고, 
-- 대여 중이지 않은 자동차인 경우 '대여 가능'을 표시하는 컬럼(컬럼명: AVAILABILITY)을 추가하여 
-- 자동차 ID와 AVAILABILITY 리스트를 출력하는 SQL문을 작성해주세요. 
-- 이때 반납 날짜가 2022년 10월 16일인 경우에도 '대여중'으로 표시해주시고 
-- 결과는 자동차 ID를 기준으로 내림차순 정렬해주세요.


-- 문제 요약
-- # 2022년 10월 16일 기준
-- # 대여 중인 자동차인 경우: '대여중' 표시
-- # 대여중이지 않은 자동차인 경우: '대여가능' 표시 
-- # '대여중', '대여가능' 둘 다 AVAILABILITY 컬럼을 만들어서 이용
-- # 출력시 주의: 반납 날짜가 2022년 10월 16일 일 경우 '대여중'으로 표시
-- # 정렬: 자동차 ID 기준 내림차순 정렬

SELECT CAR_ID, 
CASE
    WHEN CAR_ID IN (SELECT CAR_ID
                    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                    WHERE '2022-10-16' BETWEEN START_DATE AND END_DATE) THEN '대여중'
    ELSE '대여 가능'
END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC;

-- 복기사항
-- 1. CASE WHEN을 사용하여 조건에 따라 다른 값을 출력할 수 있다.
-- 2. CASE문에서 서브쿼리를 사용한 이유: 
--    CAR_ID값이 서브쿼리를 통해 이미 필터링 된 경우 동일한 CAR_ID값이 있어도 
--    CAR_ID값을 무시하고 '대여중'으로 표시되어야 하기 때문이다.(이미 대여중인 경우 대여 가능으로 표시되면 안됨)
-- 2-1. 서브쿼리는 CAR_ID 단위로 값을 반환하기 때문에, 
--      중복된 CAR_ID가 있다면 그 자체로는 중요하지 않고, 
--      해당 CAR_ID가 결과에 포함되는지 여부만 평가된다.