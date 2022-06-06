#https://leetcode.com/problems/duplicate-emails/
/* Write your PL/SQL query statement below */

/*
select Email from ( 
    select Email,count(Email) 
    from Person
    having count(Email) >1
    group by Email)
;

*/

select Email
from Person
group by Email
having count(Email) > 1
    

