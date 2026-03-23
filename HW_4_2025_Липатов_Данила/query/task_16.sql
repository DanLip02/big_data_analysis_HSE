-- Вывести полные имена всех клиентов и сотрудников в одну колонку
-- Используем UNION для объединения результатов двух запросов с одинаковыми типами колонок.
SELECT first_name || ' ' || last_name AS full_name FROM customer
UNION
SELECT first_name || ' ' || last_name FROM staff;
