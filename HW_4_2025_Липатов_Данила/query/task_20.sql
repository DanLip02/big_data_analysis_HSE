-- id, полное имя актера и посчитать в скольких фильмах снялся.
-- Группировать лучше по id, т.к. имена (имя+фамилия) могут совпадать у разных людей.
SELECT 
    a.actor_id, 
    a.first_name || ' ' || a.last_name AS full_name,
    COUNT(fa.film_id) AS film_count
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
GROUP BY a.actor_id, a.first_name, a.last_name
ORDER BY film_count DESC;
-- Актер с наибольшим количеством будет первым в списке благодаря ORDER BY DESC.
