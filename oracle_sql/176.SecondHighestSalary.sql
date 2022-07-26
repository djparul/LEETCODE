#https://leetcode.com/problems/second-highest-salary/submissions/
/*select( ifnull
       
       (select Salary from 
            (select Salary
                from employee 
                    where ROWNUM <= 2
                order by salary desc)
        where ROWNUM =1), 
   NULL) "SecondHighestSalary";
*/
/* Select MAX(Salary) AS SecondHighestSalary from Employee
where Salary < (Select MAX(Salary) from Employee); */

SELECT max(salary) AS SecondHighestSalary FROM 
(
SELECT SALARY, dense_Rank() OVER (ORDER BY SALARY DESC) RNUM
FROM Employee
 )
 WHERE RNUM = 2
