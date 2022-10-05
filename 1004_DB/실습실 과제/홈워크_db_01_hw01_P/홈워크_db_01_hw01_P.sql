
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

-- 2)
INSERT INTO zoo (rowid, name, eat, weight, age) VALUES
(10,'dolphin', 'carnivore', 210, 3),
(10, 'alligator', 'carnivore', 250, 50);

-- 3)
INSERT INTO zoo (name, eat, age) VALUES
('dolphin', 'carnivore', 3);

-- 1번 column 목록 순서와 데이터 입력 순서가 틀리다.
-- ('gorilla', 'omnivore', 210, 180, 5); 로 수정 필요.

-- 2번 column 목록에 rowid 가 2개나 있음
--'dolphin'이나 'alligator'중 하나만 삽입하거나
--'dolphin'이나 'alligator' 중 하나에서 rowid를 다른 숫자로 변경하거나
-- column목록에서 rowid 삭제하고 삽입할 2개 목록에서 해당값 10을 지우거나
