-- DML 명령어
  -- INSERT, SELECT, UPDATE, DELETE

CREATE TABLE users (
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
);


-- 작성 순서
-- select
-- from
-- where
-- group by
-- order by
-- limit
-- offset


-- csv 테이블 import
-- csv 모드 켜는 것
.mode csv
-- users.csv를 users 테이블에 import하는 것
.import users.csv users


-- SELECT
-- SELECT: 어떤 컬럼을 가져와라 / FROM: 어떤 테이블에서
SELECT first_name, age FROM users;
SELECT * FROM users;
SELECT rowid, first_name FROM users;


-- ORDER BY
-- FROM절 뒤에 위치해야함
-- ASC 오름차순 (안써도 됨), DESE 내림차순
SELECT first_name, age FROM users ORDER BY age ASC;
SELECT first_name, age FROM users ORDER BY age DESC;
SELECT first_name, age, balance FROM users 
ORDER BY age ASC, balance DESC;


-- SELECT DISTINCT
-- 조회 결과엥서 중복된 행을 제거
-- SELECT 바로 뒤에 있어야함
-- DISTINCT 뒤에 컬럼 또는 컬럼 목록 작성
-- 모든 지역 조회하기
SELECT country FROM users;
-- 중복 없이 모든 지역 조회하기
SELECT DISTINCT country FROM users;
-- 중복 없이 모든 지역 오른차순으로 조회하기
SELECT DISTINCT country FROM users ORDER BY country;
-- 이름과 지역 중복없이 조회
SELECT DISTINCT first_name, country FROM users;
-- 이름과 지역 중복없이 오름차순으로 조회
SELECT DISTINCT first_name, country FROM users ORDER BY country DESC;
-- NULL with DISTINCT
-- NULL값을 중복으로 간주 하나만 남김


-- WHERE
-- 조회시 특정 검색 조건을 지정
-- FROM 뒤에 작성
SELECT first_name, age, balance FROM users WHERE age >= 30;
SELECT first_name, age, balance FROM users WHERE age >= 30 AND balance > 500000;
SELECT first_name, last_name FROM users WHERE first_name LIKE '%호%';
SELECT first_name, country FROM users WHERE country IN ('경기도', '강원도');
SELECT first_name, country FROM users WHERE country = '경기도' OR country = '강원도';



-- LIKE
-- 패턴과 일치 기반 데이터 조회
-- 대소문자 구분하지 않음
-- % 0개이상의 문자가 올 수 있음 ex)김% : 김으로 시작하는 모든 글자 '김'만 있어도 됨
-- _ 단일(1개)문자가 있음 ex)김_ : 김으로 시작하는 두 글자
SELECT first_name FROM users WHERE first_name LIKE '%준';
SELECT first_name, phone FROM users WHERE phone LIKE '02-%';
-- 나이가 20대인 사람들의 이름과 나이 조회
SELECT first_name, age FROM users WHERE age LIKE '2_';
-- 전화번호 중간 4자리가 51로 시작하는 사람
SELECT first_name, phone FROM users WHERE phone LIKE '%-51__-%';


-- IN
-- 값이 값 목록 결과에 일치하는지 확인
-- NOT IN도 사용 가능
-- 경기도와 강원도에 살지 않는 사람
SELECT first_name, country FROM users WHERE country NOT IN ('경기도', '강원도');


-- BETWEEN
-- 값이 범위에 있는지 테스트
-- NOT BETWEEN도 사용 가능
SELECT first_name, age FROM users WHERE age BETWEEN 20 AND 30;
SELECT first_name, age FROM users WHERE age >= 20 AND age <= 30;
SELECT first_name, age FROM users WHERE age NOT BETWEEN 20 AND 30;
SELECT first_name, age FROM users WHERE age < 20 OR age > 30;


-- LIMIT
-- 결과에서 반환하는 행 수를 제한
-- OFFSET과 함께 사용하면 특정 지정된 위치에서부터 데이터 조회가능
SELECT rowid, first_name FROM users LIMIT 10;
SELECT first_name, balance FROM users ORDER BY balance DESC LIMIT 10;
SELECT first_name, age FROM users ORDER BY age LIMIT 5;
-- 11번째부터 20번째 데이터
SELECT rowid, first_name FROM users LIMIT 10 OFFSET 10;


-- AGGREGATE FUNC(집계 함수)
-- 값 집합의 최대값, 최소값, 평균, 합계 및 개수를 계산
-- GROUP BY 절과 함계 종종 사용됨
-- MAX(), MIN(), AVG(), SUM(), COUNT() 가 잇음
-- MAX(), MIN(), AVG(), SUM()은 숫자를 기준으로 계산되므로 반드시 데이터 타입이 숫자(INTEGER)여야함

-- 유저 테이블 전체 행수
SELECT COUNT(*) FROM users;
-- 30살 이상인 사람들의 평균 나이
SELECT AVG(age) FROM users WHERE age >= 30;
SELECT AVG(balance) FROM users WHERE age >= 30;


-- GROUP BY
SELECT country FROM users GROUP BY country;
-- country 기준으로 그룹화한것을 카운트하기 떄문에 *이 아닌 다른 컬럼을 넣어다 결과는 같음
SELECT country, COUNT(*) FROM users GROUP BY country;
SELECT last_name, COUNT(*) FROM users GROUP BY last_name;
-- AS를 사용해 컬럼명을 임시로 변경하여 조회할 수 있음
SELECT last_name, COUNT(*) AS number_of_name FROM users GROUP BY last_name;
SELECT last_name, COUNT(*) FROM users GROUP BY last_name ORDER BY COUNT(*) DESC;
SELECT country, AVG(age) FROM users GROUP BY country;


-- CREATE
CREATE TABLE classmates (
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  address TEXT NOT NULL
);

-- INSERT
-- 삽입
-- INSERT INTO 뒤에 데잍 삽입할 테이블을 지정
-- 테이블 이름 뒤에 쉼표로 구분된 컬럼 목록을 추가(생략가능)
  -- 단, 생략한다면 모든 컬럼에 대한 값을 지정해야함
INSERT INTO classmates (name, age, address)
VALUES ('홍길동', 23, '서울');

INSERT INTO classmates
VALUES ('홍길동', 23, '서울');

INSERT INTO classmates
VALUES 
  ('김철수', 30, '경기'),
  ('이영미', 31, '강원'),
  ('박진성', 26, '전라'),
  ('최지수', 12, '충청'),
  ('정요한', 28, '경상');

-- UPDATE
-- 수정
-- UPDATE 뒤에 테이블 지정
-- SET뒤에 어떤 컬럼을 어떻게 바꿀지 작성
-- WHERE 뒤에 어떤 행을 바꿀지 조건 지정
  -- WHERE를 안쓰면 모든 테이블의 행에 대해 수정함
-- 선택적으로 ORDER BY 및 LIMIT 절을 사용하여 업데이트할 행 수를 지정 할 수도 있음
UPDATE classmates SET name='김철수한무두루미', address='제주도' WHERE rowid = 2;

-- DELETE
-- 삭제
-- DELETE FROM 뒤에 테이블 지정
-- WHERE 뒤에 어떤 행을 지울지 조건 지정
  -- WHERE를 안쓰면 모든 행 삭제
-- 선택적으로 ORDER BY 및 LIMIT 절을 사용하여 업데이트할 행 수를 지정 할 수도 있음
DELETE FROM classmates WHERE rowid = 5;
DELETE FROM classmates WHERE name LIKE '%영%';
DELETE FROM classmates;
