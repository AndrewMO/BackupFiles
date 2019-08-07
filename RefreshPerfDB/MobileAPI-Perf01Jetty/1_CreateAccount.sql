-- Add 10K customer records for Mobile API Performance testing
-- check whether there are any gaps in customer_id
-- only 150k today
-- Wayne Ran
-- Last Modified: 2018-04-10

declare @x integer
declare @y integer
declare @z NVARCHAR(50)

USE perf01jetty
-- actually, lets just fill in the big hole from the end of current customers up to 1000000
set @x = 8010000  --max customers
set @y = 8000001
set @z = CONVERT(NVARCHAR,@y)

print convert(nvarchar, @x)

SET NOCOUNT ON 
set identity_insert CUSTOMERS on
while @y <= @x
	begin

	if not exists (select customer_id from CUSTOMERS where CUSTOMER_ID=@y) 
		begin
			insert CUSTOMERS (CUSTOMER_ID, FIRSTNAME, LASTNAME, PASSWORD1) values (@y, 'F' + @z, 'L'+ @z, @y)

			update customers set 
			city = 'Seattle'
			, customertype_id = 6
			, state = 'WA'
			, ZIPCODE = '98104'
			, ADDRESS1 = '909 Fourth Ave'
			, ADDRESS2 = 'Suite ' + @z
			, HOMEPHONE = LEFT( '804' + @z + '000000',10) 
			, WORKPHONE = LEFT( '804' + @z + '000000',10) 
			, CEllphone = LEFT( '804' + @z + '000000',10) 
			, FAXPHONE = LEFT( '804' + @z + '000000',10) 
			, PAGERPHONE = LEFT( '804' + @z + '000000',10) 
			, OTHERPHONE = LEFT( '804' + @z + '000000',10) 
			, MAILINGCITY = 'Seattle'
			, MAILINGSTATE = 'WA'
			, MAILINGZIPCODE = '98104'
			, ssn = ''
			, question = 'futureville'
			, ANSWER = 'futureville'
			, EMERGENCYFNAME1 = 'E'+ FirstName
			, EMERGENCYLNAME1 = 'E' + LastName
			, EMERGENCYPHONE1 = LEFT( '804' + @z + '000000',10)
			, EMERGENCYPHONE2 = ''
			, EMERGENCY_OTHER_PHONE1 = ''
			, EMERGENCY_OTHER_PHONE2 = ''
			, EMERGENCYRELATION1 = 'Family Member'
			, EMAIL = 'customer' + @z + '@test.com'
			, BIRTHDATE = '1/1/1990'
			, gender = CAST(RAND() AS decimal(1,0)) + 1
			, COUNTY = 'Seattle'
			, COUNTRY = 'US'
			where CUSTOMER_ID=@y
		end
	else 
		begin
			update customers set 
			RETIRED = 0
			, EMAIL = 'customer' + @z + '@test.com'
			where CUSTOMER_ID=@y
		end
  
	set @y=@y+1
	set @z = CONVERT(NVARCHAR,@y)
   
	end
set identity_insert customers off
print @z
