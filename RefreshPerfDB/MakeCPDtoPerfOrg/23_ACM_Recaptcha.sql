-- OrgDB setting script

use acm01vegasjetty

if not exists (select KEYWORDVALUE from dbo.systeminfo where keyword = 'enable_recaptcha')
begin
    INSERT INTO [dbo].[systeminfo] ([KEYWORD], [KEYWORDVALUE] ) VALUES ('enable_recaptcha', 'false' );
end
else
begin
    update systeminfo set KEYWORDVALUE = 'false' where KEYWORD = 'enable_recaptcha'
end



