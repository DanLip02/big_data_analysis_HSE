-- Вывести число, месяц и день недели в числовом эквиваленте для каждой оплаты
-- Функция EXTRACT позволяет получить нужные части даты из поля payment_date.
-- Для дня недели (isodow): 1 - Понедельник, 7 - Воскресенье.
SELECT 
    EXTRACT(day FROM payment_date) AS payment_day,
    EXTRACT(month FROM payment_date) AS payment_month,
    EXTRACT(isodow FROM payment_date) AS payment_dow
FROM payment;
