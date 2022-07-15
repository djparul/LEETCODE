# https://leetcode.com/problems/fix-names-in-a-table/
select user_id, INITCAP(name) name
from users
order by user_id
