# https://leetcode.com/problems/market-analysis-i/
select distinct user_id buyer_id, to_char(join_date, 'YYYY-MM-DD') join_date, sum(cnt) over(partition by user_id) orders_in_2019
from (
    select user_id, join_date, case when order_year = '2019' then 1 else 0 end cnt
    from(
        select u.user_id, u.join_date, to_char(order_date, 'YYYY') order_year
        from Users u
        left join Orders j
        on u.user_id = j.buyer_id
    )
)
