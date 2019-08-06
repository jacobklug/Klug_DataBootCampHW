---data analysis 1---
SELECT e.emp_no, e.last_name, e.first_name, e.gender, s.salary
FROM employees AS e
JOIN salaries AS s
	ON e.emp_no = s.emp_no;
  
---data analysis 2---
SELECT * FROM employees 
WHERE hire_date LIKE '1986%';

---data analysis 3---
SELECT dm.dept_no, d.dept_name, dm.emp_no, e.last_name, e.first_name, dm.from_date, dm.to_date
FROM dept_manager AS dm
JOIN departments AS d
	ON dm.dept_no = d.dept_id
JOIN employees AS e
	ON dm.emp_no = e.emp_no;

---data analysis 4---
SELECT e.emp_no, e.last_name, e.first_name, de.dept_no, d.dept_name
FROM employees AS e
JOIN dept_emp AS de
 	ON e.emp_no = de.emp_no
JOIN departments as d
	ON de.dept_no=d.dept_id
ORDER BY e.emp_no;

---data analysis 5---
SELECT * FROM employees 
WHERE first_name = 'Hercules'
AND last_name LIKE 'B%';

---data analysis 6---
SELECT de.emp_no, e.last_name, e.first_name, d.dept_name
FROM employees AS e
JOIN dept_emp as de
	ON e.emp_no = de.emp_no
JOIN departments as d
	on d.dept_id = de.dept_no
WHERE d.dept_name = 'Sales';

---data analysis 7---
SELECT de.emp_no, e.last_name, e.first_name, d.dept_name
FROM employees AS e
JOIN dept_emp as de
	ON e.emp_no = de.emp_no
JOIN departments as d
	on d.dept_id = de.dept_no
WHERE d.dept_name = 'Sales' OR d.dept_name = 'Development';

---data analysis 8---
SELECT last_name, count(last_name) as "Last Name Count" FROM employees 
Group by last_name
Order by "Last Name Count" DESC;
