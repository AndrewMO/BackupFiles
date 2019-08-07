-- Add family members to familyMember table
-- @Wayne Ran, 2016-05-18

declare @x integer
declare @y integer
declare @z NVARCHAR(50)
declare @sql NVARCHAR(max)
declare @sqlLoop integer

USE lstgnaparec
-- actually, lets just fill in the big hole from the end of current customers up to 1000000
set @x = 200000  -- Max customers
set @y = 100001
set @z = CONVERT(NVARCHAR,@y)
set @sqlLoop = 1

print convert(nvarchar, @x)

if exists (select familymember_id FROM FAMILYMEMBERS where (customer_id between @y and @x)
			or (customer_id between @y+10000000 and @x+10000000))
	BEGIN
		select top 100 * from FAMILYMEMBERS  where (customer_id between @y and @x) or (customer_id between @y+10000000 and @x+10000000)
		return
	END

SET NOCOUNT ON 
set @sql = 'insert FAMILYMEMBERS (customer_id, family_id, role, familyrole_id) ' 

while @y <= @x
	begin

		set @sql = @sql + ' select '+ @z + ',' + @z + ','+ '0' + ','+ '4' +' union all'
		set @sql = @sql + ' select '+ CONVERT(NVARCHAR,(@y+10000000)) + ',' + @z + ','+ '0' + ','+ '4' +' union all'
		
		if @sqlLoop = 50
		begin
			set @sql = substring(@sql,1,len(@sql)-9)
			--print @sql
			execute(@sql)
			set @sqlLoop = 0
			set @sql = 'insert FAMILYMEMBERS (customer_id, family_id, role, familyrole_id) '
		end
 
		set @sqlLoop = @sqlLoop +1
		set @y=@y+1
		set @z = CONVERT(NVARCHAR,@y)
   
	end

if len(@sql) > 70
begin	
	set @sql = substring(@sql,1,len(@sql)-9)
	execute(@sql)
	--print @sql
end 

print @y
