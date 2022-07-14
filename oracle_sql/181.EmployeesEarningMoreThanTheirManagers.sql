# https://leetcode.com/problems/employees-earning-more-than-their-managers/
select E.name as employee from employee E, employee M where M.id = E.managerId and E.salary > M.salary;
