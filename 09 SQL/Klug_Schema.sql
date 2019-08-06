CREATE TABLE employees(
	emp_no INT PRIMARY KEY,
	birth_date VARCHAR(15),
	first_name VARCHAR(20),
	last_name VARCHAR(20),
	gender VARCHAR(5),
	hire_date VARCHAR(15)
);
CREATE TABLE departments(
	dept_id VARCHAR(10) PRIMARY KEY,
	dept_name VARCHAR(20)
);
create table dept_emp(
	emp_no int NOT NULL,
	FOREIGN KEY (emp_no) REFERENCES employees(emp_no),
	dept_no VARCHAR(10),
	FOREIGN KEY (dept_no) REFERENCES departments(dept_id),
	from_date VARCHAR(15),
	to_date VARCHAR(15),
	PRIMARY KEY (emp_no, dept_no)
);
CREATE TABLE dept_manager(
	emp_no int NOT NULL,
	FOREIGN KEY (emp_no) REFERENCES employees(emp_no),
	dept_no VARCHAR(10),
	FOREIGN KEY (dept_no) REFERENCES departments(dept_id),
	from_date VARCHAR(15),
	to_date VARCHAR(15)
);
CREATE TABLE salaries(
	emp_no int NOT NULL,
	FOREIGN KEY (emp_no) REFERENCES employees(emp_no),
	salary int,
	from_date VARCHAR(15),
	to_date VARCHAR(15),	
	PRIMARY KEY (emp_no)
);
CREATE TABLE titles(
	emp_no int NOT NULL,
	FOREIGN KEY (emp_no) REFERENCES employees(emp_no),
	title VARCHAR(20) NOT NULL,
	from_date VARCHAR(15),
	to_date VARCHAR(15)
);

---
SELECT * FROM employees;
SELECT * FROM departments;
SELECT * FROM titles;
SELECT * FROM dept_emp;
SELECT * FROM salaries;
SELECT * FROM dept_manager;

