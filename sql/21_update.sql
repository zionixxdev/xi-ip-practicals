-- Practical 21 : UPDATE - Modifying Records
-- Informatics Practices (065) - Class XI
-- Aim: To modify the values already stored in a table using the UPDATE command with SET and WHERE.

USE school;

UPDATE student SET marks = 90 WHERE adm_no = 1;
UPDATE student SET city = 'Varanasi' WHERE adm_no = 4;
UPDATE student SET marks = marks + 5 WHERE class = 'XI-B';

SELECT * FROM student;
