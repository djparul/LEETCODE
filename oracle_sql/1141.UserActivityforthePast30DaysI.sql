# https://leetcode.com/problems/user-activity-for-the-past-30-days-i/
select to_char(activity_date,'YYYY-MM-DD') day, count(distinct user_id) active_users
from activity
where activity_date between '2019-06-28' and '2019-07-27'
group by activity_date;
