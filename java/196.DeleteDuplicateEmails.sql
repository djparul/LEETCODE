#https://leetcode.com/problems/delete-duplicate-emails/
# Write your MySQL query statement below

delete 
from Person 
where id NOT IN
    ( select * from  (
            select min(Id) from Person group by Email
        ) as p
    );

