-- Выручка в каждом месяце работы проката по rental_date (а не payment_date)
-- Используем LEFT JOIN между rental(r) и payment(p), так как могут быть прокаты без платежей.
SELECT 
    EXTRACT(year FROM r.rental_date) AS rental_year,
    EXTRACT(month FROM r.rental_date) AS rental_month,
    ROUND(SUM(p.amount), 1) AS revenue
FROM rental r
LEFT JOIN payment p ON r.rental_id = p.rental_id
GROUP BY 1, 2
ORDER BY 1, 2;
