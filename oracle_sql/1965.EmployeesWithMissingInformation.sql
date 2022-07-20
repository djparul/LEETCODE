(select employee_id from Employees
MINUS 
select employee_id from Salaries)
union
(select employee_id from Salaries
MINUS 
select employee_id from Employees)
