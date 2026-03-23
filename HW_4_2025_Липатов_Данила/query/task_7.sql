-- Вывести кто, когда (привести к типу date) и у кого брал диски в аренду в Июне 2005
-- Фильтруем данные за июнь 2005 года и приводим timestamp к типу date с помощью ::date.
SELECT 
    customer_id, 
    rental_date::date AS rental_date, 
    staff_id
FROM rental
WHERE rental_date >= '2005-06-01' AND rental_date < '2005-07-01';
