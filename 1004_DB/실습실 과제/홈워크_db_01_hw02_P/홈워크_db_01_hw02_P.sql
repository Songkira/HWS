CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

INSERT INTO zoo VALUES 
('gorilla', 'omnivore', 215, 180, 5),
('tiger', 'carnivore', 220, 115, 3),
('elephant', 'herbivore', 3800, 280, 10),
('dog', 'omnivore', 8, 20, 1),
('panda', 'herbivore', 80, 90, 2),
('pig', 'omnivore', 70, 45, 5);

BEGIN;
  DELETE FROM zoo
  WHERE weight < 100;
ROLLBACK;
BEGIN;
  DELETE FROM zoo
  WHERE eat = 'omnivore';
COMMIT;

SELECT COUNT(*)
FROM zoo;

-- zoo 테이블 작성
-- column 목록 name=text, eat=text, weight=int, height=int, age=int 
-- insert로 데이터 추가
-- weight column 목록에서 100 미만 데이터 삭제하고 이전 commit지점으로 작업취소하는건데
-- 이전 commit 명령어는 없으니 6개 그대로
-- eat column 목록에서 'omnivore' 인 데이터는 삭제(작업)한 결과를 물리적 디스크에 완전히 업데이트 됨.
-- 그럼 카운트 3개