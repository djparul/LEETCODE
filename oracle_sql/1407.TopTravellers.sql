# https://leetcode.com/problems/top-travellers/
select u.name , nvl(sum(r.distance), 0) travelled_distance
from Users u
left join Rides r
on u.id = r.user_id
group by r.user_id, u.name
order by travelled_distance desc, u.name
