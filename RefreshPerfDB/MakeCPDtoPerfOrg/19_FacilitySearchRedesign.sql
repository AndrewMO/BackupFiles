
use ACM01vegasJetty



if not exists (select KEYWORDVALUE from systeminfo where keyword = 'enable_new_cui_reservation_redirect')
begin
    Insert into SYSTEMINFO(KEYWORD, KEYWORDVALUE) values ('enable_new_cui_reservation_redirect', 'true') 
end
else
begin
    update systeminfo set KEYWORDVALUE = 'true' where keyword = 'enable_new_cui_reservation_redirect'
end

select * from systeminfo where keyword = 'enable_new_cui_reservation_redirect'


--check two license options "facility" "CUI Reservation to New Facility management module"



if not exists (select KEYWORDVALUE from systeminfo where KEYWORD = 'online_reservation_resource_search_skip_unavailable')
begin
insert into systeminfo (KEYWORD, KEYWORDVALUE) values ('online_reservation_resource_search_skip_unavailable', 'false')
end
else
begin
update SYSTEMINFO set KEYWORDVALUE = 'true' where KEYWORD = 'online_reservation_resource_search_skip_unavailable'

end

select * from systeminfo where keyword = 'online_reservation_resource_search_skip_unavailable'



if not exists (select KEYWORDVALUE from systeminfo where KEYWORD = 'online_reservation_resource_search_timeout_seconds')
begin
insert into systeminfo (KEYWORD, KEYWORDVALUE) values ('online_reservation_resource_search_timeout_seconds', 5)
end
else
begin
update SYSTEMINFO set KEYWORDVALUE = 30 where KEYWORD = 'online_reservation_resource_search_timeout_seconds'

end

select * from systeminfo where keyword = 'online_reservation_resource_search_timeout_seconds'