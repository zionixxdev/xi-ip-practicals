-- Practical 23 : SELECT - Retrieving Data
-- Informatics Practices (065) - Class XI
-- Aim: To retrieve data from a table using SELECT with conditions, sorting and aggregate functions.

USE school;

SELECT * FROM student;

SELECT name, marks FROM student
       WHERE marks >= 85 ORDER BY marks DESC;

SELECT COUNT(*) AS total, AVG(marks) AS average,
       MAX(marks) AS highest, MIN(marks) AS lowest
FROM student;

SELECT class, COUNT(*) AS students FROM student GROUP BY class;
