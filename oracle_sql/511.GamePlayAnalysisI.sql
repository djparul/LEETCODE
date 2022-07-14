# https://leetcode.com/problems/game-play-analysis-i/
select player_id, min(to_char(event_date, 'YYYY-MM-DD')) first_login
from activity
group by player_id 
order by player_id
