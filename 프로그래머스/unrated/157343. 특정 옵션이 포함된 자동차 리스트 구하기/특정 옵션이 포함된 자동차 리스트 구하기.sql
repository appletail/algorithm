-- 코드를 입력하세요
# SELECT *
# FROM CAR_RENTAL_COMPANY_CAR
# WHERE OPTIONS LIKE '%네비게이션%'
# ORDER BY CAR_ID DESC

SELECT *
FROM car_rental_company_car
WHERE instr(options, '네비게이션') > 0
ORDER BY car_id DESC;