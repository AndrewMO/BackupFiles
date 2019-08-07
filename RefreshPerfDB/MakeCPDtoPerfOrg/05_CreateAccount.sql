-- Add a million customer records for perf testing Rushtest, Perf01, Acm01vegas
-- check whether there are any gaps in customer_id
-- only 150k today

declare @x integer
declare @y integer
declare @z NVARCHAR(50)

USE acm01vegasjetty
-- actually, lets just fill in the big hole from the end of current customers up to 1000000
set @x = 3999999  --max customers
set @y = 1000001
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
			city = 'Dallas'
			, customertype_id = 4
			, state = 'TX'
			, ZIPCODE = '75201'
			, ADDRESS1 = '717 North Harwood Street'
			, ADDRESS2 = 'Suite ' + convert(nvarchar, CUSTOMER_ID)
			, HOMEPHONE = LEFT( '804' + convert(nvarchar, @y)+ '000000',10) 
			, WORKPHONE = LEFT( '804' + convert(nvarchar, @y)+ '000000',10) 
			, CEllphone = LEFT( '804' + convert(nvarchar, @y)+ '000000',10) 
			, FAXPHONE = LEFT( '804' + convert(nvarchar, @y)+ '000000',10) 
			, PAGERPHONE = LEFT( '804' + convert(nvarchar, @y)+ '000000',10) 
			, OTHERPHONE = LEFT( '804' + convert(nvarchar, @y)+ '000000',10) 
			, MAILINGCITY = 'Dallas'
			, MAILINGSTATE = 'TX'
			, MAILINGZIPCODE = '75201'
			, ssn = ''
			, question = 'futureville'
			, ANSWER = 'futureville'
			, EMERGENCYFNAME1 = 'E'+ FirstName
			, EMERGENCYLNAME1 = 'E' + LastName
			, EMERGENCYPHONE1 = LEFT( '804' + convert(nvarchar, @y)+ '000000',10)
			, EMERGENCYPHONE2 = ''
			, EMERGENCY_OTHER_PHONE1 = ''
			, EMERGENCY_OTHER_PHONE2 = ''
			, EMERGENCYRELATION1 = 'Family Member'
			, EMAIL = 'Mail' + @z + '@test.com'
			, PASSWORD1 = convert(nvarchar, customer_id)
			, PASSWORD2 = convert(nvarchar, customer_id)
			, BIRTHDATE = '1/1/1981'
			, gender = CAST(RAND() AS decimal(1,0)) + 1
			, COUNTY = 'Dallas'
			, COUNTRY = 'US'
			, ADDITIONAL_EMAIL = 'ADDITIONALMail' + @z + '@test.com'
			where CUSTOMER_ID=@y
		end
	else 
		begin
			update customers set 
			PASSWORD1 = convert(nvarchar, customer_id)
			, PASSWORD2 = convert(nvarchar, customer_id)
			, RETIRED = 0
			, EMAIL = 'Mail' + @z + '@test.com'
			where CUSTOMER_ID=@y
		end

		  if @y = 10000 print @z
		  else if @y = 15000 print @z
		  else if @y = 20000 print @z
		  else if @y = 25000 print @z
		  else if @y = 30000 print @z
		  else if @y = 35000 print @z
		  else if @y = 40000 print @z
		  else if @y = 45000 print @z
		  else if @y = 50000 print @z
		  else if @y = 55000 print @z
      
		  set @y=@y+1
		  set @z = CONVERT(NVARCHAR,@y)
   
	end
set identity_insert customers off
print @z
