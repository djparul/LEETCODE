# https://leetcode.com/problems/sales-analysis-iii/
select distinct(p.product_id), p.product_name 
from product p
inner join sales s
on s.product_id = p.product_id
where p.product_id not in
    ( select  s.product_id
     from sales s
     where s.sale_date not between '2019-01-01' and '2019-03-31')
