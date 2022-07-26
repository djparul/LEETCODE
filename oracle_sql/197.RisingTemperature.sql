#https://leetcode.com/problems/rising-temperature/
/* Write your PL/SQL query statement below */

select W1.id 
from Weather W1 , Weather W2
where W1.Temperature > W2.Temperature
and W2.recordDate = W1.recordDate -1;
    
    
    
    /*(
        select Temperature from Weather where recordDate=
    )*/
