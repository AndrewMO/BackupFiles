update customers set MAILINGADDRESS1 = ('717 N HARWOOD ST STE ' + convert(nvarchar,CUSTOMER_ID)) where CUSTOMER_ID between 2236371 and 2389999
update customers set MAILINGADDRESS2 = ('Suite ' + convert(nvarchar, CUSTOMER_ID)) where CUSTOMER_ID between 2236371 and 2389999
update customers set MAILINGCOUNTRY = 'US' where CUSTOMER_ID between 2236371 and 2389999