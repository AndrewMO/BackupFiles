use [ActiveNetPerformance]

update ACM01VEGASJETTY set used = 0 where customer_id between 2000000 and 4999999




Delete from ACM01VEGASJETTY where customer_id between 1000000 and 1999999

declare @x integer
declare @y integer
declare @z NVARCHAR(50)

set @x = 4999999  --max customers
set @y = 2000001
print convert(nvarchar, @x)

SET NOCOUNT ON 
set identity_insert ACM01VEGASJETTY on
while @y <= @x
	begin

	if not exists (select customer_id from ACM01VEGASJETTY where CUSTOMER_ID=@y) 
		begin
			insert ACM01VEGASJETTY (CUSTOMER_ID, USED) values (@y, 0)
		end			
	--else 
	--	begin
	--		select CUSTOMER_ID from  ACM01VEGASJETTY where CUSTOMER_ID=@y
	--	end
      
		  set @y=@y+1
		  set @z = CONVERT(NVARCHAR,@y)
   
	end
set identity_insert ACM01VEGASJETTY off
