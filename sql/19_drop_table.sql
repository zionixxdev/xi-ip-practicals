-- Practical 19 : DROP TABLE - Deleting a Table
-- Informatics Practices (065) - Class XI
-- Aim: To delete an existing table from the database using the DROP TABLE command.

USE school;

CREATE TABLE temp_data (id INT, item VARCHAR(20));
INSERT INTO temp_data VALUES (1, 'Pen'), (2, 'Book');

SELECT * FROM temp_data;

DROP TABLE temp_data;

SHOW TABLES;
