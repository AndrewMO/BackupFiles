-- Activities prep
/*
Activity Status Code:
0 - OPEN
1 - Closed
2 - Cancelled
3 - Tentative
4 - On Hold
*/

use acm01vegasjetty

-- update SEASONS set 
      -- KEYBOARDDATE = '1899-12-30 00:00:00.000',
      -- INTERNETDATE = '1899-12-30 00:00:00.000',
      -- INTERNETENDDATE = '2017-12-31 00:00:00.000'
	  -- where seasonname like '2016%'

update ACTIVITIES set 
activitygender=0
,agesmax=99
,agesmin=0
,nointernetreg=0
,enrollmax=9999
,maxenrolledonline=9999
,internetdate='12/30/1899' 
,internetenddate='12/30/1899' 
,endingdate='12/31/2021' 
,keybrdentryenddate='12/30/1899'
,DONTRESERVEFACILITIES=-1
where season_id in (42, 45, 49, 50) and activitystatus = 0

update ACTIVITYREGISTRATIONWINDOWS set
INTERNET_DATE='1/1/2019'
,INTERNET_END_DATE='12/30/1899'
,[KEYBOARD_ENTRY_DATE]='1/1/2019'
,[NON_RES_KEYBOARD_ENTRY_DATE]='1/1/2019'
,[MEMBER_KEYBOARD_ENTRY_DATE]='1/1/2019'
,[NON_RES_INTERNET_DATE]='1/1/2019'
,[MEMBER_INTERNET_DATE]='1/1/2019'
where activity_id in (select activity_id from activities where season_id in (42, 45, 49, 50) and activitystatus = 0)

update ACTIVITYSTATISTICS set number_open = 888 
where activity_id in (select activity_id from activities where season_id in (42, 45, 49, 50) and activitystatus = 0)