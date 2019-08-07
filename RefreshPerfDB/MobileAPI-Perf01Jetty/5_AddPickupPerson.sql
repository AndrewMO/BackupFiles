-- Add pick up person to DCPICKUPAUTHORIZATIONS table
-- Author: Wayne Ran,
-- Last Modified: 2018-04-10

declare @x integer
declare @y integer
declare @z NVARCHAR(50)
declare @sql NVARCHAR(max)
declare @sqlLoop integer

USE perf01jetty
-- actually, lets just fill in the big hole from the end of current customers up to 1000000
set @x = 8010000  --max customers
set @y = 8000001
set @z = CONVERT(NVARCHAR,@y)
set @sqlLoop = 1

print convert(nvarchar, @x)

if exists (select 1 FROM DCPICKUPAUTHORIZATIONS where (PICKUPCUSTOMER_ID between @y and @x)
			or (CHILDCUSTOMER_ID between @y+10000000 and @x+10000000))
	BEGIN
		select top 100 * from DCPICKUPAUTHORIZATIONS  where (PICKUPCUSTOMER_ID between @y and @x) or (CHILDCUSTOMER_ID between @y+10000000 and @x+10000000)
		return
	END

SET NOCOUNT ON 
set @sql = 'insert DCPICKUPAUTHORIZATIONS (PICKUPCUSTOMER_ID, CHILDCUSTOMER_ID, RELATION) ' 

while @y <= @x
	begin

		set @sql = @sql + ' select '+ @z + ',' + CONVERT(NVARCHAR,(@y+10000000)) + ','+ '''Parent''' +' union all'
		
		if @sqlLoop = 50
		begin
			set @sql = substring(@sql,1,len(@sql)-9)
			--print @sql
			execute(@sql)
			set @sqlLoop = 0
			set @sql = 'insert DCPICKUPAUTHORIZATIONS (PICKUPCUSTOMER_ID, CHILDCUSTOMER_ID, RELATION) '
		end
 
		set @sqlLoop = @sqlLoop +1
		set @y=@y+1
		set @z = CONVERT(NVARCHAR,@y)
   
	end

if len(@sql) > 70
begin	
	set @sql = substring(@sql,1,len(@sql)-9)
	execute(@sql)
	print @sql
end 

print @y