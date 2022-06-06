#https://leetcode.com/problems/customers-who-never-order/
/* Write your PL/SQL query statement below */
select Name "Customers" from Customers
where Id not IN
(
    select CustomerId from Orders

)
order by Name;