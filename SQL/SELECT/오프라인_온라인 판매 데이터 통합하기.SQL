-- 문제 설명
-- 다음은 어느 의류 쇼핑몰의 온라인 상품 판매 정보를 담은 ONLINE_SALE 테이블과 
-- 오프라인 상품 판매 정보를 담은 OFFLINE_SALE 테이블 입니다. 
-- ONLINE_SALE 테이블은 아래와 같은 구조로 되어있으며 ONLINE_SALE_ID, USER_ID, PRODUCT_ID, SALES_AMOUNT, SALES_DATE는 
-- 각각 온라인 상품 판매 ID, 회원 ID, 상품 ID, 판매량, 판매일을 나타냅니다.

-- Column name	Type	Nullable
-- ONLINE_SALE_ID	INTEGER	FALSE
-- USER_ID	INTEGER	FALSE
-- PRODUCT_ID	INTEGER	FALSE
-- SALES_AMOUNT	INTEGER	FALSE
-- SALES_DATE	DATE	FALSE
-- 동일한 날짜, 회원 ID, 상품 ID 조합에 대해서는 하나의 판매 데이터만 존재합니다.

-- OFFLINE_SALE 테이블은 아래와 같은 구조로 되어있으며 
-- OFFLINE_SALE_ID, PRODUCT_ID, SALES_AMOUNT, SALES_DATE는 
-- 각각 오프라인 상품 판매 ID, 상품 ID, 판매량, 판매일을 나타냅니다.

-- Column name	Type	Nullable
-- OFFLINE_SALE_ID	INTEGER	FALSE
-- PRODUCT_ID	INTEGER	FALSE
-- SALES_AMOUNT	INTEGER	FALSE
-- SALES_DATE	DATE	FALSE
-- 동일한 날짜, 상품 ID 조합에 대해서는 하나의 판매 데이터만 존재합니다.

-- 문제
-- ONLINE_SALE 테이블과 OFFLINE_SALE 테이블에서 
-- 2022년 3월의 오프라인/온라인 상품 판매 데이터의 판매 날짜, 상품ID, 유저ID, 판매량을 출력
-- OFFLINE_SALE 테이블의 판매 데이터의 USER_ID 값은 NULL 로 표시
-- 결과는 판매일을 기준으로 오름차순 정렬
-- 판매일이 같다면 상품 ID를 기준으로 오름차순 정렬
-- 상품ID까지 같다면 유저 ID를 기준으로 오름차순 정렬

SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, 
       PRODUCT_ID, 
       USER_ID, 
       SALES_AMOUNT
FROM ONLINE_SALE
WHERE YEAR(SALES_DATE) = '2022' AND MONTH(SALES_DATE) = '3'
UNION
SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, 
       PRODUCT_ID,
       NULL AS USER_ID, 
       SALES_AMOUNT
FROM OFFLINE_SALE
WHERE YEAR(SALES_DATE) = '2022' AND MONTH(SALES_DATE) = '3'
ORDER BY SALES_DATE, PRODUCT_ID, USER_ID;

-- 복기사항
-- 1. 두 테이블을 조회 할 때 JOIN 말고도 UNION을 사용 가능하다.
-- 2. UNION을 사용할 때는 SELECT 구문이 같아야 한다.
-- 3. UNION은 중복을 제거해준다. (UNION ALL은 중복을 제거하지 않는다.)
-- 4. NULL AS를 통해 UNION은 컬럼의 개수가 다른 경우에도 사용 가능하다.
-- 5. ORDER BY는 한 번 사용하면 모든 SELECT에 적용된다.