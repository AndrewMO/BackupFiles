use perf01



IF not exists (select keywordvalue from SYSTEMINFO where KEYWORD = 'enable_new_cui_account')
BEGIN
    insert into SYSTEMINFO (KEYWORD, KEYWORDVALUE) values ('enable_new_cui_account', 'true')
END
ELSE
BEGIN
    UPDATE dbo.systeminfo SET KEYWORDVALUE = 'true' WHERE KEYWORD = 'enable_new_cui_account'
END


select * from SYSTEMINFO where keyword = 'enable_new_cui_account'