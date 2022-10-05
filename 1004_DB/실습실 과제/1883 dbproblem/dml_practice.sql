CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INTEGER NOT NULL,
  height INTEGER,
  age INTEGER 
);

INSERT INTO zoo (name, eat, weight, height, age)
VALUES ('gorilla', 'omnivore', 215, 180, 5);

INSERT INTO zoo (name, eat, weight, height)
VALUES ('rabbit', 'herbivore', 3, 150);

INSERT INTO zoo
VALUES
  ('tiger', 'carnivore', 220, 115, 3),
  ('elephant', 'herbivore', 3800, 280, 10),
  ('dog', 'omnivore', 8, 20, 1);

INSERT INTO zoo (name, eat, weight, height)
VALUES ('eagle', 'carnivore', 8, 75);

INSERT INTO zoo (name, eat, weight, age)
VALUES ('dolphin', 'carnivore', 210, 3);

INSERT INTO zoo (name, eat, weight, height)
VALUES ('alligator', 'carnivore', 250, 50);

INSERT INTO zoo
VALUES
  ('panda', 'herbivore', 80, 90, 2),
  ('pig', 'omnivore', 70, 45, 5);

SELECT name, height FROM zoo;

UPDATE zoo
SET height=15
WHERE rowid = 2;

DELETE FROM zoo WHERE eat LIKE 'omnivore';
-- DELETE FROM zoo WHERE eat = 'omnivore'; 도 가능


