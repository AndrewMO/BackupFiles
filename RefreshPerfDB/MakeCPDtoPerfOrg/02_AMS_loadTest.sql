use acm01vegasjetty

if not exists (select keyword from systeminfo where keyword = 'is_load_test_system') 
	begin
		insert into systeminfo (keyword,keywordvalue) values ('is_load_test_system','true')
	end

---- Need SQL about set AMS load test server etc...
---- Manually update the AMS settings in AUI

