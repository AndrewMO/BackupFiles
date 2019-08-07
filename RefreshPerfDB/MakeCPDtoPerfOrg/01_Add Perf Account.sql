USE [ACM01vegasJetty]
GO

CREATE USER [TAN\AN_Perf] FOR LOGIN [TAN\AN_Perf]
GO

USE [ACM01vegasJetty]
GO

ALTER ROLE [db_datareader] ADD MEMBER [TAN\AN_Perf]
GO

USE [ACM01vegasJetty]
GO

ALTER ROLE [db_datawriter] ADD MEMBER [TAN\AN_Perf]
GO

USE [ACM01vegasJetty]
GO

ALTER ROLE [db_ddladmin] ADD MEMBER [TAN\AN_Perf]
GO 