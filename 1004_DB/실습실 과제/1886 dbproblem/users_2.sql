CREATE TABLE users(
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
);

UPDATE users
SET country='경기도'
WHERE first_name='옥자' AND last_name='김';

DELETE FROM users
WHERE first_name='진호' AND last_name='백';

SELECT country, MAX(balance), age FROM users
WHERE age >= 30 AND age < 40
GROUP BY country;
