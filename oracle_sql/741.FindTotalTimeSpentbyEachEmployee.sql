# https://leetcode.com/problems/find-total-time-spent-by-each-employee/
select to_char(event_day,'YYYY-MM-DD') day, emp_id, sum(out_time)-sum(in_time) total_time
from Employees
group by emp_id, to_char(event_day,'YYYY-MM-DD');
