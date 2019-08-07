-- Add Passnumber
-- Author: Wayne Ran,
-- Last Modified: 2018-04-16

declare @x integer
declare @y integer
declare @z NVARCHAR(50)
declare @sql NVARCHAR(max)
declare @sqlLoop integer

USE perf01jetty
-- actually, lets just fill in the big hole from the end of current customers up to 1000000
set @x = 8010000  -- Max customers
set @y = 8000001
set @z = CONVERT(NVARCHAR,@y)

print convert(nvarchar, @x)

while @y <= @x
	begin
		if not exists(select 1 from passes where customer_id = @z) 
		begin
			insert into PASSES (customer_id, PASSNUMBER, PASSLAYOUT_ID, TEMPORARYPASSNUMBER) values (
			@z
			, 'PERF00000' + @z
			, 3
			, 0
			)
		end

		set @y=@y+1
		set @z = CONVERT(NVARCHAR,@y)
   
	end


