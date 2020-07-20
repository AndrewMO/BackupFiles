use perf01jetty



IF NOT EXISTS(SELECT TOP 1 1 FROM sys.tables t WITH(NOLOCK)
JOIN sys.indexes i ON t.object_id = i.object_id AND i.name = 'DCSESSIONDATES__DELETED_BEGDATETIME'
WHERE SCHEMA_NAME(t.schema_id) = 'DBO' AND OBJECT_NAME(t.object_id) ='DCSESSIONDATES' AND t.type = 'U')
BEGIN
     CREATE NONCLUSTERED  INDEX [DCSESSIONDATES__DELETED_BEGDATETIME]  ON [DBO].[DCSESSIONDATES] ([DELETED],[BEGDATETIME]) INCLUDE ([DCSESSIONDATE_ID])
	 --INCLUDE ([DCSESSIONDATE_ID],[DCSESSION_ID],[FACILITY_ID],[FACILITY_SCHEDULE_ID],[ENDDATETIME],[NUMBERREGISTERED],[PENDINGREGISTRATIONS],[NUMBERWAITLISTS],[CANCELED_DATE],[AVAILABLE_FOR_TRIAL],[PENDING_TRIAL_CLASS_REGISTRATIONS],[NUMBER_TRIAL_CLASS_REGISTERED],[CLOSED_DATE],[OVERRIDE_ENROLL_MIN],[OVERRIDE_ENROLL_MAX],[ROW_VERSION])WITH (PAD_INDEX = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, ONLINE=ON, MAXDOP=0) ON [PRIMARY]
END
GO