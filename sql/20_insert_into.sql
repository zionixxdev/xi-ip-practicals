-- Practical 20 : INSERT INTO - Adding Records
-- Informatics Practices (065) - Class XI
-- Aim: To insert new rows into the student table using the INSERT INTO command.

USE school;

INSERT INTO student VALUES (1, 'Aditya Shakya', 'XI-A', 87, 'Lucknow');
INSERT INTO student VALUES (2, 'Priya Verma', 'XI-A', 92, 'Kanpur');
INSERT INTO student VALUES (3, 'Rahul Singh', 'XI-B', 75, 'Agra');
INSERT INTO student (adm_no, name, class, marks)
       VALUES (4, 'Neha Gupta', 'XI-B', 81);
INSERT INTO student VALUES (5, 'Aman Tiwari', 'XI-A', 68, 'Lucknow');

SELECT * FROM student;
