-- Вывести адреса всех магазинов (подзапрос)
-- Используем подзапрос к таблице store, чтобы получить address_id, а затем выводим адреса.
SELECT address
FROM address
WHERE address_id IN (SELECT address_id FROM store);
