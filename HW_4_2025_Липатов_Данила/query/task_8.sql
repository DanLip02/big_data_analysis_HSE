-- Фильмы выпущенные после 2000 года, длительностью от 60 до 120 мин. Первые 20 по длительности.
-- Применяем множественные условия в WHERE, сортировку ORDER BY и LIMIT.
SELECT title, description, length
FROM film
WHERE release_year > 2000 
  AND length BETWEEN 60 AND 120
ORDER BY length DESC
LIMIT 20;
