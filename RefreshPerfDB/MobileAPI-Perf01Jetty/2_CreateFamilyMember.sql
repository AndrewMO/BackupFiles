-- Add family members to customer table
-- Author: Wayne Ran,
-- Last Modified: 2018-04-10

declare @x integer
declare @y integer
declare @z NVARCHAR(50)
declare @totalCustomer integer

USE perf01jetty
-- actually, lets just fill in the big hole from the end of current customers up to 1000000
set @x = 8010000  --max customers
set @y = 8000001

set @z = CONVERT(NVARCHAR,@y)

-- If missing any customerID between @y and @x, then quit this script!
set @totalCustomer = (select count(*) from customers where customer_id between @y and @x)
if @totalCustomer < (@x-@y+1)
	begin
		print 'Missing Customer! Quit!'
		select @totalCustomer
		return
	end

-- If exists family member which customerID between @y+10000000 and @x+10000000, the quit this script!
if exists(select customer_id from CUSTOMERS where CUSTOMER_ID between (@y+10000000) and (@x+10000000))
	begin
		select top 100 * from CUSTOMERS where CUSTOMER_ID between (@y+10000000) and (@x+10000000)
		return
	end
		
print convert(nvarchar, @x)

SET NOCOUNT ON 
set identity_insert CUSTOMERS on
while @y <= @x
	begin
			insert CUSTOMERS (
			customer_id
			, FIRSTNAME
			, LASTNAME
			, customertype_id
			, city
			, state
			, ZIPCODE 
			, ADDRESS1
			, ADDRESS2 
			, HOMEPHONE 
			, WORKPHONE  
			, CEllphone  
			, FAXPHONE  
			, PAGERPHONE  
			, OTHERPHONE  
			, MAILINGCITY  
			, MAILINGSTATE  
			, MAILINGZIPCODE  
			, BIRTHDATE
			, GENDER
			,IS_ENC_PASSWORD  			
			) values (
			@y + 10000000
			, 'FamilyOfF' + @z
			, 'L'+ @z
			, 6
			, 'Seattle'
			, 'WA'
			, '98104'
			, '909 Fourth Ave'
			, 'Suite ' +  @z
			, LEFT( '804' +  @z + '000000',10) 
			, LEFT( '804' +  @z + '000000',10) 
			, LEFT( '804' +  @z + '000000',10) 
			, LEFT( '804' +  @z + '000000',10) 
			, LEFT( '804' +  @z + '000000',10) 
			, LEFT( '804' +  @z + '000000',10) 
			, 'Seattle' 
			, 'WA' 
			, '98104' 
			, '1/1/2012'
			, CAST(RAND() AS decimal(1,0)) + 1
			, 0
			)
     
		  set @y = @y + 1
		  set @z = CONVERT(NVARCHAR,@y)
   
	end

set identity_insert customers off
print @z
