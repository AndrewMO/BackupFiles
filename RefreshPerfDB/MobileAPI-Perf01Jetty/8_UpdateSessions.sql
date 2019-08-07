-- Author: Wayne Ran
-- Last modified: 2018-04-09
-- WARNING: We have to update session from & to date one by one manually or by Neoload scripts. 
-- Site_id = 5: Bellevue Family YMCA

use perf01jetty

update DCSESSIONS
set WEEKDAYS = '0111110'
, ENROLLMIN = 1
, ENROLLMAX = 999
, BEGINNINGDATE = '2018-04-01 00:00:00.000'
, ENDINGDATE = '2018-12-30 00:00:00.000'
where dcsession_id in 
(select s.dcsession_id from dcprograms as p,[DCPROGRAMSESSIONS] as ps,dcsessions as s, [PROGRAMTYPES] as pt
where p.dcprogram_id = ps.dcprogram_id
and ps.dcsession_id = s.dcsession_id
and s.programtype_id = pt.programtype_id
and p.dcprogram_id in (5983,5984,5988,5989,6116,6060,6061,6062,6063,6070,6071,5992,5993,5994,5995,5996,5997,6121,6127,6128,6129,6130,6131,6132,6133,6134,6135,6136,5436,5437)
and p.site_id =5
)

update stages
set showonline = 0
, signatureline = 0
, REQUIRED_BEFORE_COMPLETING_TRANSACTION = 0
, REQUIRE_INITIALS_ONLINE = 0

update ATTACHEDCHECKLISTITEMS
set showonline = 0
, signatureline = 0
, REQUIRED_BEFORE_COMPLETING_TRANSACTION = 0
, REQUIRE_INITIALS_ONLINE = 0
, ITEMSIGNEDONLINE = 0
where dcprogram_id in (5983,5984,5988,5989,6116,6060,6061,6062,6063,6070,6071,5992,5993,5994,5995,5996,5997,6121,6127,6128,6129,6130,6131,6132,6133,6134,6135,6136,5436,5437)


select DCSESSION_ID,PROGRAMTYPE_ID,SITE_ID, FACILITY_ID, DCSESSIONNAME from DCSESSIONS
where dcsession_id in 
(select s.dcsession_id from dcprograms as p,[DCPROGRAMSESSIONS] as ps,dcsessions as s, [PROGRAMTYPES] as pt
where p.dcprogram_id = ps.dcprogram_id
and ps.dcsession_id = s.dcsession_id
and s.programtype_id = pt.programtype_id
and p.dcprogram_id in (5983,5984,5988,5989,6116,6060,6061,6062,6063,6070,6071,5992,5993,5994,5995,5996,5997,6121,6127,6128,6129,6130,6131,6132,6133,6134,6135,6136,5436,5437)
and p.site_id =5
)