# https://leetcode.com/problems/sales-analysis-iii/
select p.product_id, p.product_name 
from product p where product_id not in
    ( select  s.product_id
     from sales s
     where s.sale_date not between '2019-01-01' and '2019-03-31')
