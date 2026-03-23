-- Создание weekly_revenue (если еще нет) и расчет накопленной суммы
-- Используем оконную функцию SUM(revenue) OVER (ORDER BY r_year, r_week)
CREATE TABLE IF NOT EXISTS weekly_revenue AS
SELECT 
    EXTRACT(year FROM r.rental_date) AS r_year,
    EXTRACT(week FROM r.rental_date) AS r_week,
    SUM(p.amount) AS revenue
FROM rental r 
LEFT JOIN payment p ON p.rental_id = r.rental_id 
GROUP BY 1, 2 
ORDER BY 1, 2;

SELECT 
    r_year, 
    r_week, 
    revenue,
    ROUND(SUM(revenue) OVER (ORDER BY r_year, r_week)) AS cumulative_revenue
FROM weekly_revenue;
