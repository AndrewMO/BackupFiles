use ACM01vegasJetty



select * from SYSTEMINFO where keyword = 'org_cache_copies'

insert into SYSTEMINFO (KEYWORD, KEYWORDVALUE) values ('org_cache_copies', 3)

select * from SYSTEMINFO where keyword = 'org_cache_copies'