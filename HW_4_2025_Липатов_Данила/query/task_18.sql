-- Кто (customer_id), когда (rental_date дата) и у кого (staff_id) брал диски в июне 2005
-- Этот запрос очень похож на задание 7, выводим с группировкой/фильтром.
SELECT 
    customer_id, 
    rental_date::date AS rental_date, 
    staff_id
FROM rental
WHERE rental_date >= '2005-06-01' AND rental_date < '2005-07-01';
