


use ACM01vegasJetty



IF not exists (select keywordvalue from SYSTEMINFO where KEYWORD = 'enable_new_cui_activity_search_redirect')
BEGIN
    insert into SYSTEMINFO (KEYWORD, KEYWORDVALUE) values ('enable_new_cui_activity_search_redirect', 'true')
END
ELSE
BEGIN
    UPDATE SYSTEMINFO SET KEYWORDVALUE = 'true' where KEYWORD = 'enable_new_cui_activity_search_redirect'
END





IF not exists (select keywordvalue from SYSTEMINFO where KEYWORD = 'enable_activity_enrollment_redesign')
BEGIN
    insert into SYSTEMINFO (KEYWORD, KEYWORDVALUE) values ('enable_activity_enrollment_redesign', 'true')
END
ELSE
BEGIN
    UPDATE SYSTEMINFO SET KEYWORDVALUE = 'true' where KEYWORD = 'enable_activity_enrollment_redesign'
END








––select count(*) from activities
––where season_id in (42, 43, 44, 45)
––and activitystatus = 0
––and hideoninternet > -1
––and onlineteamassign <> -1
––and allow_team_add_online <> -1
––and teamplayermax = 0
––and allow_team_add  <> -1
––and activity_type_id in (7,12)
––and TEAMENROLLMENTSONLY <> -1
––and show_type_selection <> -1
––and activity_id not in(select activity_id from [dbo].[PREREQUISITES])