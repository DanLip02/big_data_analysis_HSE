-- Средний платеж по каждому жанру фильма. Отобразить жанры, где более 60 фильмов.
-- Последовательно соединяем payment -> rental -> inventory -> film -> film_category -> category
SELECT 
    c.name AS category_name,
    ROUND(AVG(p.amount), 2) AS avg_payment_amount
FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
JOIN inventory i ON fc.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN payment p ON r.rental_id = p.rental_id
GROUP BY c.category_id, c.name
HAVING COUNT(DISTINCT fc.film_id) > 60
ORDER BY avg_payment_amount DESC;
