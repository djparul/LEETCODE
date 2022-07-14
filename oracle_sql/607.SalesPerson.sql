# https://leetcode.com/problems/sales-person/
select name from salesperson
where sales_id not in (
    select sales_id 
        from orders 
        where com_id in ( 
            select com_id from company
            where company.name = 'RED'
        )
)
