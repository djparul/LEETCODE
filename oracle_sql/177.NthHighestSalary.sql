# https://leetcode.com/problems/nth-highest-salary/
CREATE FUNCTION getNthHighestSalary(N IN NUMBER) RETURN NUMBER IS
res NUMBER;
BEGIN
    /* Write your PL/SQL query statement below */
    select salary into res from (select distinct(salary), rank() over (order by salary desc) as r from employee group by salary) where r = N;
    RETURN res;
END;
