
use ACM01vegasJetty



IF not exists (select keywordvalue from SYSTEMINFO where KEYWORD = 'enable_new_cui_activity_search_redirect')
BEGIN
    insert into SYSTEMINFO (KEYWORD, KEYWORDVALUE) values ('enable_new_cui_activity_search_redirect', 'true')
END
ELSE
BEGIN
    update systeminfo set KEYWORDVALUE = 'true' where KEYWORD = 'enable_new_cui_activity_search_redirect'
END