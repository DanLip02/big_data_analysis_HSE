-- Вывести количество уникальных имен клиентов
-- Использование COUNT вместе с ключевым словом DISTINCT.
SELECT COUNT(DISTINCT first_name) AS unique_names_count
FROM customer;
