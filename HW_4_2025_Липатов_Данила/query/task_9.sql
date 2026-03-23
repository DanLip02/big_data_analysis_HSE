-- Платежи в апреле 2007, стоимость не превышает 4 доллара. По убыванию стоимости.
-- Сортируем по amount DESC, а при совпадении - по payment_date ASC.
SELECT payment_id, payment_date::date AS payment_date, amount
FROM payment
WHERE payment_date >= '2007-04-01' AND payment_date < '2007-05-01'
  AND amount <= 4
ORDER BY amount DESC, payment_date ASC;
