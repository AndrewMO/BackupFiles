-- Enable cache contorl for test site
-- @Wayne Ran, 2017-04-07

USE acm01vegasjetty


if not exists (select 1 FROM systeminfo where KEYWORD = 'enable_cache_control_for_non_prod_site')
	BEGIN
		insert into systeminfo (keyword,keywordvalue) values ('enable_cache_control_for_non_prod_site','true')
	END



