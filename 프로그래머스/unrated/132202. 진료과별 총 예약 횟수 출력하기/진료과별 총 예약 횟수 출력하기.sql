-- 코드를 입력하세요
# FROM APPOINTMENT 테이블에서 
# WHERE 2022년 5월에 예약한 환자 수를 진료과코드 별로 조회
# SELECT '진료과 코드', '5월예약건수'로 지정해주시고 결과는 
# ORDER BY 진료과별 예약한 환자 수를 기준 오름차순 정렬하고, 진료과 코드를 기준으로 오름차순 정렬
SELECT MCDP_CD AS '진료과코드', COUNT(*) AS '5월예약건수'
FROM APPOINTMENT
WHERE APNT_YMD LIKE '2022-05%'
GROUP BY MCDP_CD
ORDER BY 5월예약건수, 진료과코드