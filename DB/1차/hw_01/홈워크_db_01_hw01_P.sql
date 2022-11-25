
CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

-- 1) 
INSERT INTO zoo VALUES 
(5, 180, 210, 'gorilla', 'omnivore');
name, eat, weight, height age 순으로 작성하여야하는데 반대로 작성하여 형식이 안맞기 때문에 오류가 남

-- 2)
INSERT INTO zoo (rowid, name, eat, weight, age) VALUES
(10,'dolphin', 'carnivore', 210, 3),
(10, 'alligator', 'carnivore', 250, 50);
같은 rowid를 작성하여 pk가 중복되기 때문에 오류가 남

-- 3)
INSERT INTO zoo (name, eat, age) VALUES
('dolphin', 'carnivore', 3);
weight가 NOT NULL 속성인데 작성을 안해 오류가 나