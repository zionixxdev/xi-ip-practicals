-- Practical 18 : CREATE TABLE - Creating a Table
-- Informatics Practices (065) - Class XI
-- Aim: To create a table named student in MySQL using the CREATE TABLE command with suitable data types and a PRIMARY KEY constraint.

CREATE DATABASE IF NOT EXISTS school;
USE school;

CREATE TABLE student (
    adm_no INT PRIMARY KEY,
    name   VARCHAR(30) NOT NULL,
    class  VARCHAR(5),
    marks  INT,
    city   VARCHAR(20)
);

DESC student;
