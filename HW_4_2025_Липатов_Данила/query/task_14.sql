-- Вывести число ячеек в инвентаре каждого магазина
-- Связываем таблицы store и inventory (или просто считаем по store_id из inventory).
SELECT store_id, COUNT(inventory_id) AS inventory_count
FROM inventory
GROUP BY store_id;
