use acm01vegasjetty

update systeminfo set keywordvalue = '/opt/active/ActiveNet/perf/SQLBACKUPS/acm01vegasjetty' where keyword = 'full_backup_unc'
update systeminfo set keywordvalue = 'W:\perf\SQLBACKUPS\acm01vegasjetty' where keyword = 'full_backup_unc_remote'
update systeminfo set keywordvalue = 'X:\acm01vegasjetty' where keyword = 'image_storage_path'
update systeminfo set keywordvalue = '/opt/active/data/an_filedata/acm01vegasjetty' where keyword = 'image_storage_path_local'
update systeminfo set keywordvalue = '/acm01vegasjetty/jreport/' where keyword = 'jreport_jsp_path'

select * from systeminfo where keyword in ('full_backup_unc','full_backup_unc_remote','image_storage_path','image_storage_path_local','jreport_jsp_path')

-- Manually disable DB automatic backup at 'Web Admin' -> 'Active Staff'






