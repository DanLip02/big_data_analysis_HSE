-- Вывести имена клиентов, которые не совпадают с именами сотрудников (except)
-- Оператор EXCEPT возвращает строки из первого запроса, которых нет во втором.
SELECT first_name FROM customer
EXCEPT
SELECT first_name FROM staff;
