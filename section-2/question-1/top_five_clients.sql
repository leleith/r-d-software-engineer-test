select a.*
from (
    select
        customer_id,
        sum(amount) as total_purchase
    from
        orders
    group by
        customer_id
) a
order by a.total_purchase desc
limit 5