
use ACM01vegasJetty


-- login
IF not exists (select keywordvalue from SYSTEMINFO where KEYWORD = 'enable_new_cui_account')
BEGIN
    insert into SYSTEMINFO (KEYWORD, KEYWORDVALUE) values ('enable_new_cui_account', 'true')
END
ELSE
BEGIN
    update systeminfo set KEYWORDVALUE = 'true' where KEYWORD = 'enable_new_cui_account'
END

select * from dbo.systeminfo where keyword = 'enable_new_cui_account'


--myaccount
IF not exists (select keywordvalue from SYSTEMINFO where KEYWORD = 'myaccount_redesign_on_cui')
BEGIN
    insert into SYSTEMINFO (KEYWORD, KEYWORDVALUE) values ('myaccount_redesign_on_cui', 'true')
END
ELSE
BEGIN
    update systeminfo set KEYWORDVALUE = 'true' where KEYWORD = 'myaccount_redesign_on_cui'
END

select * from dbo.systeminfo where keyword = 'enable_new_cui_account'
