-- Создать таблицу студентов(id, имя, фамилия, возраст, дата рождения, адрес)
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
