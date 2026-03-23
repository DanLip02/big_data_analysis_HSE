-- Вывести сумму, дату и день недели для каждой оплаты (текстом)
-- To_char преобразует дату в строку. 'Day' выдает день недели текстом.
SELECT 
    amount, 
    payment_date::date AS payment_date,
    TO_CHAR(payment_date, 'Day') AS day_of_week
FROM payment;
