import os

queries = {
    1: """-- Вывести список всех клиентов (customer)
-- Мы просто выбираем все колонки из таблицы customer.
SELECT * FROM customer;
""",
    2: """-- Вывести список имен и фамилий клиентов с именем Carolyn
-- Используем фильтрацию WHERE по колонке first_name.
SELECT first_name, last_name 
FROM customer 
WHERE first_name = 'Carolyn';
""",
    3: """-- Вывести полные имена клиентов (имя + фамилия), имя или фамилия которых содержит “ary”
-- Используем оператор LIKE для поиска подстроки 'ary' (с учетом регистра или ILIKE без учета)
-- Оператор || используется для конкатенации строк со пробелом.
SELECT first_name || ' ' || last_name AS full_name
FROM customer
WHERE first_name ILIKE '%ary%' OR last_name ILIKE '%ary%';
""",
    4: """-- Вывести 20 самых крупных транзакций (payment)
-- Сортируем по полю amount по убыванию и ограничиваем вывод с помощью LIMIT 20.
SELECT *
FROM payment
ORDER BY amount DESC
LIMIT 20;
""",
    5: """-- Вывести адреса всех магазинов (подзапрос)
-- Используем подзапрос к таблице store, чтобы получить address_id, а затем выводим адреса.
SELECT address
FROM address
WHERE address_id IN (SELECT address_id FROM store);
""",
    6: """-- Вывести число, месяц и день недели в числовом эквиваленте для каждой оплаты
-- Функция EXTRACT позволяет получить нужные части даты из поля payment_date.
-- Для дня недели (isodow): 1 - Понедельник, 7 - Воскресенье.
SELECT 
    EXTRACT(day FROM payment_date) AS payment_day,
    EXTRACT(month FROM payment_date) AS payment_month,
    EXTRACT(isodow FROM payment_date) AS payment_dow
FROM payment;
""",
    7: """-- Вывести кто, когда (привести к типу date) и у кого брал диски в аренду в Июне 2005
-- Фильтруем данные за июнь 2005 года и приводим timestamp к типу date с помощью ::date.
SELECT 
    customer_id, 
    rental_date::date AS rental_date, 
    staff_id
FROM rental
WHERE rental_date >= '2005-06-01' AND rental_date < '2005-07-01';
""",
    8: """-- Фильмы выпущенные после 2000 года, длительностью от 60 до 120 мин. Первые 20 по длительности.
-- Применяем множественные условия в WHERE, сортировку ORDER BY и LIMIT.
SELECT title, description, length
FROM film
WHERE release_year > 2000 
  AND length BETWEEN 60 AND 120
ORDER BY length DESC
LIMIT 20;
""",
    9: """-- Платежи в апреле 2007, стоимость не превышает 4 доллара. По убыванию стоимости.
-- Сортируем по amount DESC, а при совпадении - по payment_date ASC.
SELECT payment_id, payment_date::date AS payment_date, amount
FROM payment
WHERE payment_date >= '2007-04-01' AND payment_date < '2007-05-01'
  AND amount <= 4
ORDER BY amount DESC, payment_date ASC;
""",
    10: """-- Имена, фамилии и идентификаторы клиентов с именами Jack, Bob, Sara, фамилия с "p"
-- Переименовываем колонки с помощью AS "Имя". Сортировка по возрастанию id.
SELECT 
    first_name AS "Имя", 
    last_name AS "Фамилия", 
    customer_id AS "Идентификатор"
FROM customer
WHERE first_name IN ('Jack', 'Bob', 'Sara')
  AND last_name ILIKE '%p%'
ORDER BY customer_id ASC;
""",
    11: """-- Создать таблицу студентов(id, имя, фамилия, возраст, дата рождения, адрес)
-- Выполняем набор DDL (Data Definition Language) и DML (Data Manipulation Language) команд.

-- 1. Создание таблицы с ограничением NOT NULL
CREATE TABLE student (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    birth_date DATE NOT NULL,
    address VARCHAR(200) NOT NULL
);

-- 2. Вносим 1 студента с id > 50
INSERT INTO student (id, first_name, last_name, age, birth_date, address)
VALUES (51, 'Ivan', 'Ivanov', 20, '2004-05-15', 'Moscow, Pushkin st.');

-- 3. Вывод записей
SELECT * FROM student;

-- 4. Вносим несколько записей с автоинкрементным id
INSERT INTO student (first_name, last_name, age, birth_date, address)
VALUES 
    ('Anna', 'Smirnova', 19, '2005-02-10', 'Saint Petersburg, Nevsky pr.'),
    ('Petr', 'Petrov', 21, '2003-11-20', 'Kazan, Bauman st.');

-- 5. Вывод записей
SELECT * FROM student;

-- 6. Удаление 1 студента на выбор (например, Ivan)
DELETE FROM student WHERE id = 51;

-- 7. Вывод списка студентов
SELECT * FROM student;

-- 8. Удаление таблицы
DROP TABLE student;
""",
    12: """-- Вывести количество уникальных имен клиентов
-- Использование COUNT вместе с ключевым словом DISTINCT.
SELECT COUNT(DISTINCT first_name) AS unique_names_count
FROM customer;
""",
    13: """-- 5 самых частых сумм оплаты, их даты, количество и сумма платежей одинакового номинала
-- Группируем по сумме и дате документа, считаем количество и сумму через агрегатные функции.
SELECT 
    amount, 
    payment_date::date AS payment_date, 
    COUNT(*) AS count_payments, 
    SUM(amount) AS total_amount
FROM payment
GROUP BY amount, payment_date::date
ORDER BY COUNT(*) DESC
LIMIT 5;
""",
    14: """-- Вывести число ячеек в инвентаре каждого магазина
-- Связываем таблицы store и inventory (или просто считаем по store_id из inventory).
SELECT store_id, COUNT(inventory_id) AS inventory_count
FROM inventory
GROUP BY store_id;
""",
    15: """-- Вывести адреса всех магазинов (JOIN)
-- Вместо подзапроса используем JOIN таблиц store и address по ключу address_id.
SELECT s.store_id, a.address
FROM store s
JOIN address a ON s.address_id = a.address_id;
""",
    16: """-- Вывести полные имена всех клиентов и сотрудников в одну колонку
-- Используем UNION для объединения результатов двух запросов с одинаковыми типами колонок.
SELECT first_name || ' ' || last_name AS full_name FROM customer
UNION
SELECT first_name || ' ' || last_name FROM staff;
""",
    17: """-- Вывести имена клиентов, которые не совпадают с именами сотрудников (except)
-- Оператор EXCEPT возвращает строки из первого запроса, которых нет во втором.
SELECT first_name FROM customer
EXCEPT
SELECT first_name FROM staff;
""",
    18: """-- Кто (customer_id), когда (rental_date дата) и у кого (staff_id) брал диски в июне 2005
-- Этот запрос очень похож на задание 7, выводим с группировкой/фильтром.
SELECT 
    customer_id, 
    rental_date::date AS rental_date, 
    staff_id
FROM rental
WHERE rental_date >= '2005-06-01' AND rental_date < '2005-07-01';
""",
    19: """-- id всех клиентов с 40+ оплатами. Средний размер транзакции всех клиентов, округлить до 2
-- Используем GROUP BY для подсчета оплат и HAVING для фильтрации (>= 40).
-- Для среднего - Оконная функция или подзапрос. Здесь используем просто агрегацию по клиенту.
-- "Посчитать средний размер для всех клиентов" - возможно общая средняя, или средняя этого клиента.
SELECT 
    customer_id, 
    COUNT(payment_id) AS payment_count,
    ROUND(AVG(amount), 2) AS avg_amount
FROM payment
GROUP BY customer_id
HAVING COUNT(payment_id) >= 40;
""",
    20: """-- id, полное имя актера и посчитать в скольких фильмах снялся.
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
""",
    21: """-- Выручка в каждом месяце работы проката по rental_date (а не payment_date)
-- Используем LEFT JOIN между rental(r) и payment(p), так как могут быть прокаты без платежей.
SELECT 
    EXTRACT(year FROM r.rental_date) AS rental_year,
    EXTRACT(month FROM r.rental_date) AS rental_month,
    ROUND(SUM(p.amount), 1) AS revenue
FROM rental r
LEFT JOIN payment p ON r.rental_id = p.rental_id
GROUP BY 1, 2
ORDER BY 1, 2;
""",
    22: """-- Средний платеж по каждому жанру фильма. Отобразить жанры, где более 60 фильмов.
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
""",
    23: """-- Какие фильмы чаще всего берут напрокат по субботам? Топ 5.
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
""",
    24: """-- Вывести сумму, дату и день недели для каждой оплаты (текстом)
-- To_char преобразует дату в строку. 'Day' выдает день недели текстом.
SELECT 
    amount, 
    payment_date::date AS payment_date,
    TO_CHAR(payment_date, 'Day') AS day_of_week
FROM payment;
""",
    25: """-- Распределить фильмы в три категории по длительности. Рассчитать количество прокатов и фильмов
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
""",
    26: """-- Создание weekly_revenue (если еще нет) и расчет накопленной суммы
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
""",
    27: """-- Рассчитать скользящую среднюю недельной выручки бизнеса
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
""",
    28: """-- Посчитать прирост недельной выручки бизнеса в %
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
"""
}

# Create output dir
os.makedirs('queries', exist_ok=True)

for i in range(1, 29):
    filename = f'task_{i}.sql'
    with open(filename, 'w') as f:
        f.write(queries[i])
    print(f"Created {filename}")
