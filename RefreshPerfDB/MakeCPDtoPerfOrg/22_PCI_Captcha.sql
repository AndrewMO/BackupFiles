-- OrgDB setting script

delete from dbo.systeminfo where keyword = 'enable_pci_captcha'
INSERT into dbo.SYSTEMINFO
    (KEYWORD, KEYWORDVALUE)
VALUES
    ('enable_pci_captcha', 'false')
select *
from dbo.systeminfo
where keyword = 'enable_pci_captcha'


if not exists (select KEYWORDVALUE from dbo.systeminfo where keyword = 'enable_pci_captcha')
begin
    insert into systeminfo (KEYWORD,KEYWORDVALUE) VALUES ('enable_pci_captcha','false')
end
else
begin
    update systeminfo set KEYWORDVALUE = 'false' where KEYWORD = 'enable_pci_captcha'
end

select * from dbo.systeminfo where keyword = 'enable_pci_captcha'


-- Sites DB setting

delete from dbo.systeminfo where keyword = 'enable_pci_captcha'
INSERT into dbo.SYSTEMINFO
    (CONFIGURATION_ID,KEYWORD, KEYVALUE)
VALUES
    (1, 'enable_pci_captcha', 'false')
select *
from dbo.systeminfo
where keyword = 'enable_pci_captcha'



if not exists (select KEYWORDVALUE from dbo.systeminfo where keyword = 'enable_pci_captcha')
begin
    insert into systeminfo (KEYWORD,KEYWORDVALUE) VALUES ('enable_pci_captcha','false')
end
else
begin
    update systeminfo set KEYWORDVALUE = 'false' where KEYWORD = 'enable_pci_captcha'
end

select * from dbo.systeminfo where keyword = 'enable_pci_captcha'

