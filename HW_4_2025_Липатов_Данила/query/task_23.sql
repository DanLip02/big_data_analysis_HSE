-- Какие фильмы чаще всего берут напрокат по субботам? Топ 5.
-- Извлекаем isodow = 6 (суббота), считаем количество прокатов фильма, сортируем.
SELECT 
    f.title, 
    COUNT(r.rental_id) AS rental_count
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
WHERE EXTRACT(isodow FROM r.rental_date) = 6
GROUP BY f.film_id, f.title
ORDER BY rental_count DESC, f.title ASC
LIMIT 5;
