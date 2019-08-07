use perf01jetty

select distinct customer_id,dcprogram_id into #tempCustomers
from transactions 
where customer_id > 18000000
and transaction_id > 3872959

select tc.customer_id,c.firstname,c.LASTNAME, c.homephone, p.PASSNUMBER , tc.dcprogram_id, ak.alternatekey_id
from #tempCustomers as tc
left join customers as c on tc.customer_id = c.customer_id
left join passes as p on tc.customer_id = p.customer_id
left join CUSTOMER_ALTERNATE_KEYS as ak on ak.customer_id = tc.customer_id