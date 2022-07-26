#https://leetcode.com/problems/combine-two-tables/
/* Write your PL/SQL query statement below */
/* FirstName, LastName, City, State */
select Person.FirstName, Person.LastName, Address.City, Address.State 
from Person 
left join Address
on Person.PersonId = Address.PersonId ;
/*and T.Address is not null;*/
