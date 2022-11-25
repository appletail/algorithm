-- DDL.sql 명령넣는 곳
-- mydb.sqlite3 데이터베이스 저장
-- sql의 언어(.을 안쓰는 명령어)는 ;을 쓰기 전까지는 명령이 종료된 것이 아님
-- 터미널에서 .을 쓰는 명령어는 db 서버 시스템 자체에게 하는 것
-- 터미널에서 .을 안쓰는 명령어는 sql로 명령 하는 것
-- sqlite3 mydb.sqlite3 콘솔에서 바로 데이터베이스를 여는 것
-- sqlite3 / .open mydb.sqlite3 sqlite를 켠 후에 데이터베이스를 여는 것
-- 사실 소문자, 대문자 구분 안함. 하지만 표준에 따라 달라짐. 지금 같은 경우에는 장고에 따라서 하는 중


-- DDL 명령어
  -- CREATE, ALTER, DROP

-- sql 명령어
-- 테이블 생성
CREATE TABLE contacts(
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  email TEXT NOT NULL UNIQUE
);

CREATE TABLE students(
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  email TEXT NOT NULL UNIQUE
);



-- 테이블 이름 변경
ALTER TABLE contacts RENAME TO new_contacts;

-- 컬럼 이름 변경
ALTER TABLE new_contacts RENAME COLUMN name TO last_name;

-- 새컬럼 추가(not null을 하는데 기존의 값이 있는 경우 default를 주면 됨)
ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL DEFAULT 'no address';

-- 컬럼 삭제
ALTER TABLE new_contacts DROP COLUMN address;
-- 삭제 못하는 경우
  -- FOREIGN KEY로 쓰이는 경우
  -- PRIMARY KEY 인 경우
  -- UNIQUE 제약 조건이 있는 경우


-- 테이블 삭제
DROP TABLE new_contacts;
