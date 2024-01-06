-- 코드를 입력하세요
# SELECT
#     HISTORY_ID,
#     CAR_ID, 
#     DATE_FORMAT(START_DATE, '%Y-%m-%d') AS START_DATE,
#     DATE_FORMAT(END_DATE, '%Y-%m-%d') AS END_DATE,
#     CASE
#         WHEN DATEDIFF(END_DATE, START_DATE) + 1 >= 30 THEN '장기 대여'
#         ELSE '단기 대여'
#     END AS RENT_TYPE
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# WHERE START_DATE LIKE '2022-09%' 
# ORDER BY HISTORY_ID DESC

 SELECT HISTORY_ID,
        CAR_ID,
        date_format(start_date ,'%Y-%m-%d'),
        date_format(end_date ,'%Y-%m-%d'), 
case when  DATEDIFF(end_date,start_date)+1 >=30 then '장기 대여'
else '단기 대여'
end as RENT_TYPE
from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
where DATE_FORMAT(START_DATE, '%Y-%m') = '2022-09'
order by 1 desc