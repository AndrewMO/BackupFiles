use acm01vegasjetty



if not exists (select keywordvalue from systeminfo where KEYWORD = 'new_cui_url')
BEGIN
    insert into systeminfo (KEYWORD,KEYWORDVALUE) VALUES ('new_cui_url','https://ancperf.apm.activecommunities.com')
END
else
BEGIN
    update systeminfo set KEYWORDVALUE = 'https://ancperf.apm.activecommunities.com' where KEYWORD = 'new_cui_url'
END