use acm01vegasjetty



select * from systeminfo where keyword like '%cache%' 

--INSERT INTO systeminfo (KEYWORD,KEYWORDVALUE) VALUES ('org_cache_mode','NATIVE')

update systeminfo set KEYWORDVALUE = 'LOCAL' where KEYWORD = 'org_cache_mode'

select * from systeminfo where keyword like '%cache%' 