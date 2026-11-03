-- Practical 22 : DELETE - Removing Records
-- Informatics Practices (065) - Class XI
-- Aim: To remove selected rows from a table using the DELETE command with the WHERE clause.

USE school;

DELETE FROM student WHERE adm_no = 5;
DELETE FROM student WHERE city = 'Kanpur';

SELECT * FROM student;
