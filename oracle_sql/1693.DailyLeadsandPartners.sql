# https://leetcode.com/problems/daily-leads-and-partners/
select to_char(date_id,'YYYY-MM-DD') DATE_ID, make_name, count(distinct lead_id) unique_leads
, count(distinct partner_id) unique_partners
from DailySales
group by date_id, make_name
