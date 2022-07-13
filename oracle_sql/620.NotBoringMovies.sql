# https://leetcode.com/problems/not-boring-movies/
select id, movie, description, rating
from cinema
where description not like 'boring' and mod(id,2) <> 0
order by rating desc;
