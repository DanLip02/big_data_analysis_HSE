-- Вывести адреса всех магазинов (JOIN)
-- Вместо подзапроса используем JOIN таблиц store и address по ключу address_id.
SELECT s.store_id, a.address
FROM store s
JOIN address a ON s.address_id = a.address_id;
