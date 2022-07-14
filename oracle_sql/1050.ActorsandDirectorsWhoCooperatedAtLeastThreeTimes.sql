# https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/
select actor_id, director_id from 
(
    select actor_id, director_id, count(timestamp)
    from actordirector
    group by actor_id, director_id
    having count(timestamp) >= 3
    order by actor_id, director_id
)
