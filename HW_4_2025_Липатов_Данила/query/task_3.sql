-- Вывести полные имена клиентов (имя + фамилия), имя или фамилия которых содержит “ary”
-- Используем оператор LIKE для поиска подстроки 'ary' (с учетом регистра или ILIKE без учета)
-- Оператор || используется для конкатенации строк со пробелом.
SELECT first_name || ' ' || last_name AS full_name
FROM customer
WHERE first_name ILIKE '%ary%' OR last_name ILIKE '%ary%';
