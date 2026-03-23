-- 5 самых частых сумм оплаты, их даты, количество и сумма платежей одинакового номинала
-- Группируем по сумме и дате документа, считаем количество и сумму через агрегатные функции.
SELECT 
    amount, 
    payment_date::date AS payment_date, 
    COUNT(*) AS count_payments, 
    SUM(amount) AS total_amount
FROM payment
GROUP BY amount, payment_date::date
ORDER BY COUNT(*) DESC
LIMIT 5;
