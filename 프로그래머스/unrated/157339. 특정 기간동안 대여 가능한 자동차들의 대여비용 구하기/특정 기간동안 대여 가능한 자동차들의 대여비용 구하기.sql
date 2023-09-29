-- 코드를 입력하세요
 # WHERE
 # 1. 자동차 종류가 '세단' 또는 'SUV' 인 자동차 중 
 # 2. 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능하고 
 # 3. 30간의 대여 금액이 50만원 이상 200만원 미만인 자동차
 # SELECT
 # 자동차 ID, 자동차 종류, 대여 금액(컬럼명: FEE) 리스트를 출력하는 SQL문을 작성해주세요. 
 # ORDER BY
 # 1. 대여 금액을 기준으로 내림차순 정렬
 # 2. 자동차 종류를 기준으로 오름차순 정렬
 # 3. 자동차 ID를 기준으로 내림차순 정렬
SELECT
    CRCC.CAR_ID,
    CRCC.CAR_TYPE,
    FLOOR(CRCC.DAILY_FEE * (1 - CRCDP.DISCOUNT_RATE * 0.01)) * 30 AS FEE
FROM
    CAR_RENTAL_COMPANY_CAR AS CRCC
    JOIN (SELECT *
          FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
          GROUP BY CAR_ID
          HAVING MIN(START_DATE) >= '2022-11-30' OR
                 MAX(END_DATE) <= '2022-11-1') AS CRCRH 
    JOIN (SELECT * 
          FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
          WHERE DURATION_TYPE = '30일 이상') AS CRCDP
    ON CRCC.CAR_ID = CRCRH.CAR_ID AND CRCC.CAR_TYPE = CRCDP.CAR_TYPE
WHERE
    CRCC.CAR_TYPE IN ('세단', 'SUV') AND
    CRCRH.START_DATE >= '2022-11-30' OR CRCRH.END_DATE <= '2022-11-1' AND
    FLOOR(CRCC.DAILY_FEE * (1 - CRCDP.DISCOUNT_RATE * 0.01)) * 30 >= 500000 AND
    FLOOR(CRCC.DAILY_FEE * (1 - CRCDP.DISCOUNT_RATE * 0.01)) * 30 < 2000000
ORDER BY 
    FEE DESC,
    CRCC.CAR_TYPE,
    CRCC.CAR_ID DESC