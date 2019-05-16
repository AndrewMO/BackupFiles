use acm01vegasjetty


if not exists (select * from systeminfo where keyword = 'enable_ignite_monitor')
	BEGIN
		insert into  systeminfo (KEYWORD,KEYWORDVALUE) values ('enable_ignite_monitor', 'false')
	END
else 
	BEGIN
		update systeminfo set KEYWORDVALUE = 'false' where KEYWORD = 'enable_ignite_monitor'
	END	

select * from systeminfo where keyword = 'enable_ignite_monitor'