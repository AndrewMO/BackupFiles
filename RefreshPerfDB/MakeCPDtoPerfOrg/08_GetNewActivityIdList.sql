-- Don't use the activity which have prerequisites
use acm01vegasjetty

select activity_id,activitynumber from activities
where season_id in (42, 45, 49, 50)
and activitystatus = 0
and hideoninternet > -1
and onlineteamassign <> -1  
and allow_team_add_online <> -1
and teamplayermax = 0
and allow_team_add  <> -1
and activity_id not in(select activity_id from [dbo].[PREREQUISITES])