CREATE DATABASE Corporation;

USE Corporation;

CREATE TABLE Employees (
    Department_name VARCHAR(50) NOT NULL,
    Employee_id INT NOT NULL,
    Employee_name VARCHAR(50) NOT NULL
);

CREATE TABLE Salaries (
    Salary INT NOT NULL,
    Employee_id INT NOT NULL,
    Employee_name VARCHAR(50) NOT NULL
);

-- Now populating both tables
INSERT INTO Employees
(Department_name, Employee_id, Employee_name)
VALUES
('Sales', 123, 'John Doe'),
('Sales', 211, 'Jane Smith'),
('HR', 556, 'Billy Bob'),
('Sales', 711, 'Robert Hayek'),
('Marketing', 235, 'Edward Jorgson'),
('Marketing', 236, 'Christine Packard');

INSERT INTO Salaries
(Salary, Employee_id, Employee_name)
VALUES
(500, 123, 'John Doe'),
(600, 211, 'Jane Smith'),
(1000, 556, 'Billy Bob'),
(400, 711, 'Robert Hayek'),
(1200, 235, 'Edward Jorgson'),
(200, 236, 'Christine Packard');