use perf02



IF not exists (select keywordvalue from SYSTEMINFO where KEYWORD = 'enable_facility_dressing_room')
BEGIN
    insert into SYSTEMINFO (KEYWORD, KEYWORDVALUE) values ('enable_facility_dressing_room', 'true')
END
ELSE
BEGIN
    UPDATE dbo.systeminfo SET KEYWORDVALUE = 'true' WHERE KEYWORD = 'enable_facility_dressing_room'
END


select * from SYSTEMINFO where keyword = 'enable_facility_dressing_room'