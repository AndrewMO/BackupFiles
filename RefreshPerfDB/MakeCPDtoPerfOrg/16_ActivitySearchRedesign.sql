use acm01vegasjetty



if not exists (select keywordvalue from systeminfo where KEYWORD = 'enable_new_cui_activity_search_redirect')
BEGIN
    insert into systeminfo (KEYWORD,KEYWORDVALUE) VALUES ('enable_new_cui_activity_search_redirect','true')
END
else
BEGIN
    update systeminfo set KEYWORDVALUE = 'true' where KEYWORD = 'enable_new_cui_activity_search_redirect'
END


select * from systeminfo where KEYWORD = 'enable_new_cui_activity_search_redirect'


