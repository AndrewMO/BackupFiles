-- Add Alternate Key 
-- @Wayne Ran, 2018-03-21

declare @x integer
declare @y integer
declare @z NVARCHAR(50)
declare @sql NVARCHAR(max)
declare @sqlLoop integer

USE perf01jetty
-- actually, lets just fill in the big hole from the end of current customers up to 1000000
set @x = 18010000  -- Max customers
set @y = 18000001
set @z = CONVERT(NVARCHAR,@y)

print convert(nvarchar, @x)

while @y <= @x
	begin
		if not exists(select 1 from CUSTOMER_ALTERNATE_KEYS where customer_id = @z) 
		begin
			insert into CUSTOMER_ALTERNATE_KEYS (customer_id, ALTERNATEKEYTYPE_ID, ALTERNATEKEYSTATUS_ID, ALTERNATEKEY_ID) values (
			'1'+ @z
			, '106'
			, '119'
			, 'AK' + '1'+ @z
			)
		end

		set @y=@y+1
		set @z = CONVERT(NVARCHAR,@y)
   
	end


ALTERNATEKEYTYPE_ID
106

ALTERNATEKEYSTATUS_ID
119

ALTERNATEKEY_ID
AK18000001