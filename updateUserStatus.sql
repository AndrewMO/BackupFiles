declare @customerid integer
declare @used bit
declare @end integer

set @used = 0
set @end = 1100000  
set @customerid = 1000001

SET NOCOUNT ON 
set IDENTITY_INSERT lstgbreckenridgerec ON


update lstgbreckenridgerec set used = 1 where customer_id between 100000 and 199999

while @customerid < @end
    begin 
	if not exists (select USED from lstgbreckenridgerec where CUSTOMER_ID = @customerid )
	begin
	    insert into lstgbreckenridgerec (CUSTOMER_ID,USED) VALUES (@customerid , @used )
	    

	end
	ELSE
	begin
	    update lstgbreckenridgerec set USED= @used where CUSTOMER_ID = @customerid		
	end
	set @customerid=@customerid+1
	end

set IDENTITY_INSERT lstgbreckenridgerec OFF