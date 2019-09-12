create table #DB_Size_Summary
(
    stg_db_name nvarchar(50),
    stg_db_size nvarchar(50)
)





use LSTGApacheJunction

declare @pages int  
declare @dbname sysname  
declare @dbsize dec(15,0)  
declare @logsize dec(15)  
declare @bytesperpage dec(15,0)  
declare @pagesperMB  dec(15,0)  
 
 select @dbsize = sum(convert(dec(15),size))  
  from dbo.sysfiles  
  where (status & 64 = 0)  
   
 select @logsize = sum(convert(dec(15),size))  
  from dbo.sysfiles  
  where (status & 64 <> 0)  
   
 select @bytesperpage = low  
  from master.dbo.spt_values  
  where number = 1  
   and type = 'E'  
 select @pagesperMB = 1048576 / @bytesperpage  


insert into #DB_Size_Summary 
   
 select   database_name = db_name(),  
  database_size =  
   ltrim(str((@dbsize + @logsize) / @pagesperMB,15,2) + ' MB')








select * from #DB_Size_Summary


drop table  #DB_Size_Summary