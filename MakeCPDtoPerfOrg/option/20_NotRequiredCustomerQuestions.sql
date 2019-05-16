use acm01vegasjetty



update [dbo].[ACTIVITYCUSTOMQUESTIONS] set 
questionorder = 0,
required = 0,
DO_NOT_SHOW_AFTER = '2017-12-30 00:00:00.000'
where activity_id in (
select activity_id from activities where season_id in (36, 38, 39, 40) and activitystatus = 0
)