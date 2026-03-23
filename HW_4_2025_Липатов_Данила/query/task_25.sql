-- Распределить фильмы в три категории по длительности. Рассчитать количество прокатов и фильмов
-- Используем CASE для категорий. Используем LEFT JOIN с rental для учета фильмов без прокатов.
SELECT 
    CASE 
        WHEN f.length < 70 THEN 'Короткие'
        WHEN f.length >= 70 AND f.length < 130 THEN 'Средние'
        ELSE 'Длинные' 
    END AS duration_category,
    COUNT(DISTINCT f.film_id) AS film_count,
    COUNT(r.rental_id) AS rental_count
FROM film f
LEFT JOIN inventory i ON f.film_id = i.film_id
LEFT JOIN rental r ON i.inventory_id = r.inventory_id
GROUP BY duration_category;
