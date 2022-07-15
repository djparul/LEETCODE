# https://leetcode.com/problems/calculate-special-bonus/
select employee_id, case when mod(employee_id,2) = 0 or
          name like 'M%'
    then 0 else salary end as bonus
from employees
order by employee_id
