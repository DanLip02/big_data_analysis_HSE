-- Вывести 20 самых крупных транзакций (payment)
-- Сортируем по полю amount по убыванию и ограничиваем вывод с помощью LIMIT 20.
SELECT *
FROM payment
ORDER BY amount DESC
LIMIT 20;
