IF EXISTS (SELECT * FROM tempdb.sys.all_objects WHERE name like '%#DBSize%')
      DROP TABLE DBO.#DBSize
    
CREATE TABLE #DBSize
(
      DBName varchar(100),
      DBStatus varchar(20),
      Recovery_Model varchar(100),
      Database_Path varchar(500),
      File_Size float,
      Space_Used float,
      Free_Space float,
      File_Size_String Varchar(100),
      Space_Used_String Varchar(100),
      Free_Space_String Varchar(100)
)
 
 
insert into #DBSize(Dbname, DBStatus, Recovery_Model, Database_Path, file_Size, Space_Used, Free_Space)
exec sp_msforeachdb
'USE [?];
  SELECT DB_NAME() AS DbName,
    CONVERT(varchar(20),DatabasePropertyEx(''?'',''Status'')) ,
    CONVERT(varchar(20),DatabasePropertyEx(''?'',''Recovery'')),
    physical_name,
      size*8.00 AS File_Size,
      FILEPROPERTY(name, ''SpaceUsed'')*8.00 as Space_Used,
      size*8.00 - FILEPROPERTY(name, ''SpaceUsed'')*8.00 AS Free_Space
FROM sys.database_files -- where type in 0
'
 
UPDATE #DBSize SET
      File_Size_String =
            CASE
                  WHEN File_Size/1024.00 > 1000 THEN Convert(Varchar(50),Convert(decimal(20,2),(File_Size/1024/1024.00))) + ' GB'
                  ELSE Convert(Varchar(50),Convert(decimal(20,2),(File_Size/1024.00))) + ' MB'
            END,
      Space_Used_String =
            CASE
                  WHEN Space_Used/1024.00 > 1000 THEN Convert(Varchar(50),Convert(decimal(20,2),(Space_Used/1024/1024.00))) + ' GB'
                  ELSE Convert(Varchar(50),Convert(decimal(20,2),(Space_Used/1024.00))) + ' MB'
            END,
      Free_Space_String =
            CASE
                  WHEN Free_Space/1024.00 > 1000 THEN Convert(Varchar(50),Convert(decimal(20,2),(Free_Space/1024/1024.00))) + ' GB'
                  ELSE Convert(Varchar(50),Convert(decimal(20,2),(Free_Space/1024.00))) + ' MB'
            END 
 
 
 
SELECT DBName, DBStatus, Recovery_Model, File_Size_String, Space_Used_String, Free_Space_String, Database_Path
FROM #DBSize
ORDER BY File_Size DESC, Space_Used DESC, Free_Space DESC,DBName
     
--SELECT * FROM #DBSize
 
 
IF EXISTS (SELECT * FROM tempdb.sys.all_objects WHERE name like '%#DBSize%')
      DROP TABLE #dbsize
    