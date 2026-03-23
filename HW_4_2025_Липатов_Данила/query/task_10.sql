-- Имена, фамилии и идентификаторы клиентов с именами Jack, Bob, Sara, фамилия с "p"
-- Переименовываем колонки с помощью AS "Имя". Сортировка по возрастанию id.
SELECT 
    first_name AS "Имя", 
    last_name AS "Фамилия", 
    customer_id AS "Идентификатор"
FROM customer
WHERE first_name IN ('Jack', 'Bob', 'Sara')
  AND last_name ILIKE '%p%'
ORDER BY customer_id ASC;
