# https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/
select customer_number  from 
(
    select customer_number, count(order_number) c
    from orders
    group by customer_number
    order by c desc
) where rownum = 1
