

use acm01vegas




IF not exists (select keywordvalue from SYSTEMINFO where KEYWORD = 'org_cache_copies')
BEGIN
    insert into SYSTEMINFO (KEYWORD, KEYWORDVALUE) values ('org_cache_copies', 1)
END
ELSE
BEGIN
    UPDATE SYSTEMINFO SET KEYWORDVALUE = 1 where KEYWORD = 'org_cache_copies'
END


select * from SYSTEMINFO where KEYWORD = 'org_cache_copies'