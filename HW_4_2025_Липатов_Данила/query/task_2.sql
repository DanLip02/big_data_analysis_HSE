-- Вывести список имен и фамилий клиентов с именем Carolyn
-- Используем фильтрацию WHERE по колонке first_name.
SELECT first_name, last_name 
FROM customer 
WHERE first_name = 'Carolyn';
