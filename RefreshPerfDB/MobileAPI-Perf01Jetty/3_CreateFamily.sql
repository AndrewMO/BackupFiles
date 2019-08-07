-- Make sure there are already customer which ID between 1000001 - 9999999
-- Author: Wayne Ran,
-- Last Modified: 2018-04-10

declare @x integer
declare @y integer
declare @z NVARCHAR(50)
declare @totalCustomer integer
declare @sql NVARCHAR(max)
declare @sqlLoop integer

USE perf01jetty

set @x = 8010000  --max customers
set @y = 8000001
set @z = CONVERT(NVARCHAR,@y)

set @sqlLoop = 1

-- If missing any customerID between @y and @x, then quit this script!
set @totalCustomer = (select count(*) from customers where customer_id between @y and @x)
if @totalCustomer < (@x-@y+1)
	begin
		print 'Missing Customer! Quit!'
		select @totalCustomer
		return
	end

print convert(nvarchar, @x)

SET NOCOUNT ON 
SET identity_insert FAMILIES on

set @sql = 'insert into FAMILIES (FAMILY_ID, FAMILYNAME, EXTERNALID)' 

while @y <= @x
	begin
		if not exists (select FAMILY_ID FROM FAMILIES where FAMILY_ID = @y )
			BEGIN
				set @sql = @sql + ' select '+ @z + ', ' + '''L' + @z + ''','+ '0' + ' union all'
			END

		if @sqlLoop = 100
		begin
			set @sql = substring(@sql,1,len(@sql)-9)
			--print @sql
			execute(@sql)
			set @sqlLoop = 0
			set @sql = 'insert into FAMILIES (FAMILY_ID, FAMILYNAME, EXTERNALID) ' 
		end

		set @sqlLoop = @sqlLoop +1
		set @y=@y+1
		set @z = CONVERT(NVARCHAR,@y) 
	end

if len(@sql) > 60
begin	
	set @sql = substring(@sql,1,len(@sql)-9)
	execute(@sql)
	--print @sql
end 

SET identity_insert FAMILIES off
print @sql
print @z
