-- Рассчитать скользящую среднюю недельной выручки бизнеса
-- Используем оконную функцию с рамкой PRECEDING и FOLLOWING для недели до, текущей, и после.
SELECT 
    r_year, 
    r_week, 
    revenue,
    ROUND(SUM(revenue) OVER (ORDER BY r_year, r_week)) AS cumulative_revenue,
    ROUND(AVG(revenue) OVER (
        ORDER BY r_year, r_week 
        ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
    )) AS moving_average
FROM weekly_revenue;
