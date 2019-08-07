-- Wayne Ran @ 04-08-2018
-- Choose 30 programs and update them in AUI manually, each program should only have 1 session, choose which have center prior than others. 
-- Note for 'having count(dcprogram_id) =1', we cannot use scripts to enroll daycare program which have multiple session
-- RG_CATEGORY_ID = 29 : Learning & Enrichment
-- Choose 30 daycare programs for Mobile API performance testing

select * from dcprograms where dcprogram_id in
(select dcprogram_id from [dbo].[DCPROGRAMSESSIONS] where dcprogram_id in 
(select dcprogram_id from dcprograms where site_id = 5 and INTERNET_DATE > '2017-09-01 00:00:00.000' ) 
group by dcprogram_id
having count(dcprogram_id) =1
)
order by agesmax desc

-- Update programs 
update DCPROGRAMS
set KEYBOARD_ENTRY_DATE = '2018-04-01 00:00:00.000'
, KEYBOARD_ENTRY_END_DATE = '2018-12-31 00:00:00.000'
, INTERNET_DATE = '2018-04-01 00:00:00.000'
, INTERNET_END_DATE = '2018-12-31 00:00:00.000'
, AGESMIN = 1
, AGESMAX = 16
, RETIRED = 0
, HIDEONINTERNET = 0
, STATUS = 0
, IS_SEARCHABLE = -1
, SHOW_PRICE_INFO_ONLINE = -1
, DEFAULT_PAYMENT_CYCLE = 0
where site_id = 5 
and dcprogram_id in (5983,5984,5988,5989,6116,6060,6061,6062,6063,6070,6071,5992,5993,5994,5995,5996,5997,6121,6127,6128,6129,6130,6131,6132,6133,6134,6135,6136,5436,5437)

select p.site_id,p.dcprogram_id,p.catalognumber,s.dcsession_id,s.facility_id,s.programtype_id,s.dcsessionname,s.description 
from dcprograms as p,[DCPROGRAMSESSIONS] as ps,dcsessions as s, [PROGRAMTYPES] as pt
where p.dcprogram_id = ps.dcprogram_id
and ps.dcsession_id = s.dcsession_id
and s.programtype_id = pt.programtype_id
and p.dcprogram_id in
(select dcprogram_id from [dbo].[DCPROGRAMSESSIONS] where dcprogram_id in 
(5983,5984,5988,5989,6116,6060,6061,6062,6063,6070,6071,5992,5993,5994,5995,5996,5997,6121,6127,6128,6129,6130,6131,6132,6133,6134,6135,6136,5436,5437) 
group by dcprogram_id
)