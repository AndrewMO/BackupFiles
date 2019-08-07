-- Only use one site is enough for Mobile API performance testing, just use site_id = 5
-- Each program have a ‘Site ID', but may not have a 'Center ID'.
-- By Wayne Ran
-- Last modified: 2018-3-2

use perf01jetty

select top 100 * from [dbo].[DCSESSIONS] order by endingdate desc

select site_id, count(1) as sessionsNumberPerSite from [DCSESSIONS]
group by site_id
order by sessionsNumberPerSite desc

select site_id,count(1) as programNum from [dbo].[DCPROGRAMS]
group by site_id
order by programNum desc

select * from [dbo].[SITES] where site_id = 5

select top 100 * from [DCSESSIONS] 
where site_id = 5 
and endingdate > '2016-01-01 00:00:00.000'

select top 100 status, * from [dbo].[DCPROGRAMS] 
where catalognumber in( 44276,49474,49480,44317)

select status, count(1) as sta from [DCPROGRAMS]
where site_id in (5,9) and INTERNET_DATE > '2016-01-01 00:00:00.000'
group by status


select p.programtype,* from dcsessions as d inner join PROGRAMTYPES as p on d.programtype_id = p.programtype_id
where d.site_id in (5,9) and d.beginningdate >= '2016-01-01 00:00:00.000'

select s.dcsessionname,pt.programtype,s.site_id,p.site_id as psite_id,p.dcprogramname,p.catalognumber from dcprograms as p,[DCPROGRAMSESSIONS] as ps,dcsessions as s, [PROGRAMTYPES] as pt
where p.dcprogram_id = ps.dcprogram_id
and ps.dcsession_id = s.dcsession_id
and s.programtype_id = pt.programtype_id
and p.dcprogram_id in
(select dcprogram_id from [dbo].[DCPROGRAMSESSIONS] where dcprogram_id in 
(select dcprogram_id from dcprograms where site_id = 5 and INTERNET_DATE > '2016-01-01 00:00:00.000' ) 
group by dcprogram_id
having count(dcprogram_id) =1)
and p.site_id =5 and p.dcprogram_id < 3227)
order by site_id

select p.catalognumber,p.dcprogram_id,s.dcsession_id,s.programtype_id,p.site_id,s.facility_id,s.dcsessionname,s.description 
from dcprograms as p,[DCPROGRAMSESSIONS] as ps,dcsessions as s, [PROGRAMTYPES] as pt
where p.dcprogram_id = ps.dcprogram_id
and ps.dcsession_id = s.dcsession_id
and s.programtype_id = pt.programtype_id
and p.dcprogram_id in
(select dcprogram_id from [dbo].[DCPROGRAMSESSIONS] where dcprogram_id in 
(select dcprogram_id from dcprograms where site_id in (5,9) and INTERNET_DATE > '2016-01-01 00:00:00.000' ) 
group by dcprogram_id
having count(dcprogram_id) =1)
and ( p.site_id = 9 or (p.site_id =5 and p.dcprogram_id < 3227))
order by site_id

select count(*) from [DCPROGRAMCUSTOM_QUESTION_GROUPS] 

select * from [DCPROGRAMCUSTOM_QUESTION_GROUPS] where dcprogram_id in (
select p.dcprogram_id from dcprograms as p,[DCPROGRAMSESSIONS] as ps,dcsessions as s, [PROGRAMTYPES] as pt
where p.dcprogram_id = ps.dcprogram_id
and ps.dcsession_id = s.dcsession_id
and s.programtype_id = pt.programtype_id
and p.dcprogram_id in
(select dcprogram_id from [dbo].[DCPROGRAMSESSIONS] where dcprogram_id in 
(select dcprogram_id from dcprograms where site_id in (5,9) and INTERNET_DATE > '2016-01-01 00:00:00.000' ) 
group by dcprogram_id
having count(dcprogram_id) =1)
and ( p.site_id = 9 or (p.site_id =5 and p.dcprogram_id < 3227))
)