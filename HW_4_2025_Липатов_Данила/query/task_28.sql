-- Посчитать прирост недельной выручки бизнеса в %
-- Используем оконную функцию LAG для получения значения предыдущей строки.
WITH revenue_data AS (
    SELECT 
        r_year, 
        r_week, 
        revenue,
        ROUND(SUM(revenue) OVER (ORDER BY r_year, r_week)) AS cumulative_revenue,
        ROUND(AVG(revenue) OVER (ORDER BY r_year, r_week ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING)) AS moving_average,
        LAG(revenue) OVER (ORDER BY r_year, r_week) AS prev_revenue
    FROM weekly_revenue
)
SELECT 
    r_year, 
    r_week, 
    revenue,
    cumulative_revenue,
    moving_average,
    ROUND((revenue - prev_revenue) / prev_revenue * 100, 2) AS growth_percentage
FROM revenue_data;
