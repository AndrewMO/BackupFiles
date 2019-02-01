use perf01

--Clear real emails 
UPDATE dbo.SYSTEM_USERS set EMAIL = 'xx_' + EMAIL where EMAIL <> '';
UPDATE dbo.CUSTOMERS set EMAIL = 'xx_' + EMAIL where EMAIL <> '';
UPDATE dbo.CUSTOMERS set ADDITIONAL_EMAIL = 'xx_' + ADDITIONAL_EMAIL where ADDITIONAL_EMAIL <> '';
UPDATE dbo.COMPANIES set EMAIL= 'xx_' + EMAIL where EMAIL <> '';
UPDATE dbo.INSTRUCTORS SET EMAIL = 'test@test.com' WHERE EMAIL <>'';

UPDATE dbo.SYSTEMINFO SET keywordvalue = 'xx_' + convert(varchar,keywordvalue) where keyword ='account_change_email' AND datalength(KEYWORDVALUE) > 0;
UPDATE dbo.SYSTEMINFO SET keywordvalue = 'xx_' + convert(varchar,keywordvalue) where keyword ='attack_alert_email' AND datalength(KEYWORDVALUE) > 0;
UPDATE dbo.SYSTEMINFO SET keywordvalue = 'xx_' + convert(varchar,keywordvalue) where keyword ='auto_payment_email_failed_address_from' AND datalength(KEYWORDVALUE) > 0;
UPDATE dbo.SYSTEMINFO SET keywordvalue = 'xx_' + convert(varchar,keywordvalue) where keyword ='auto_renewal_email_failed_address_from' AND datalength(KEYWORDVALUE) > 0;
UPDATE dbo.SYSTEMINFO SET keywordvalue = 'xx_' + convert(varchar,keywordvalue) where keyword ='auto_payment_email_successful_address_from' AND datalength(KEYWORDVALUE) > 0;
UPDATE dbo.SYSTEMINFO SET keywordvalue = 'xx_' + convert(varchar,keywordvalue) where keyword ='auto_renewal_email_successful_address_from' AND datalength(KEYWORDVALUE) > 0;
UPDATE dbo.SYSTEMINFO SET keywordvalue = 'xx_' + convert(varchar,keywordvalue) where keyword ='contact_email' AND datalength(KEYWORDVALUE) > 0;
UPDATE dbo.SYSTEMINFO SET keywordvalue = 'xx_' + convert(varchar,keywordvalue) where keyword ='email_service_user_name' AND datalength(KEYWORDVALUE) > 0;
UPDATE dbo.SYSTEMINFO SET keywordvalue = 'xx_' + convert(varchar,keywordvalue) where keyword ='online_registration_notification' AND datalength(KEYWORDVALUE) > 0;
UPDATE dbo.SYSTEMINFO SET keywordvalue = 'xx_' + convert(varchar,keywordvalue) where keyword ='online_reservation_notification' AND datalength(KEYWORDVALUE) > 0;
UPDATE dbo.SYSTEMINFO SET keywordvalue = 'xx_' + convert(varchar,keywordvalue) where keyword ='permit_expiry_email' AND datalength(KEYWORDVALUE) > 0;
UPDATE dbo.SYSTEMINFO SET keywordvalue = 'xx_' + convert(varchar,keywordvalue) where keyword ='pos_reorder_email' AND datalength(KEYWORDVALUE) > 0;
UPDATE dbo.SYSTEMINFO SET keywordvalue = 'xx_' + convert(varchar,keywordvalue) where keyword ='queued_receipts_email' AND datalength(KEYWORDVALUE) > 0;
UPDATE dbo.SYSTEMINFO SET keywordvalue = 'xx_' + convert(varchar,keywordvalue) where keyword ='rcia_email' AND datalength(KEYWORDVALUE) > 0;
UPDATE dbo.SYSTEMINFO SET keywordvalue = 'xx_' + convert(varchar,keywordvalue) where keyword ='romailfromaddress' AND datalength(KEYWORDVALUE) > 0;
UPDATE dbo.SYSTEMINFO SET keywordvalue = 'xx_' + convert(varchar,keywordvalue) where keyword ='romailfromname' AND datalength(KEYWORDVALUE) > 0;
UPDATE dbo.SYSTEMINFO SET keywordvalue = 'xx_' + convert(varchar,keywordvalue) where keyword ='servlet_admin_email' AND datalength(KEYWORDVALUE) > 0;

UPDATE dbo.SITEINFO SET keywordvalue = 'xx_' + convert(varchar, keywordvalue) where keyword ='contact_email' AND datalength(KEYWORDVALUE) > 0;
UPDATE dbo.SITEINFO SET keywordvalue = 'xx_' + convert(varchar, keywordvalue) where keyword ='registration_notification_email' AND datalength(KEYWORDVALUE) > 0;
UPDATE dbo.SITEINFO SET keywordvalue = 'xx_' + convert(varchar, keywordvalue) where keyword ='romailfromaddress' AND datalength(KEYWORDVALUE) > 0;
UPDATE dbo.SITEINFO SET keywordvalue = 'xx_' + convert(varchar, keywordvalue) where keyword ='romailfromname' AND datalength(KEYWORDVALUE) > 0;

-- delete the bcc values, as they can be a list of email addresses
delete from dbo.SYSTEMINFO where keyword ='auto_payment_email_failed_address_bcc' AND datalength(KEYWORDVALUE) > 0;
delete from dbo.SYSTEMINFO where keyword ='auto_payment_email_successful_address_bcc' AND datalength(KEYWORDVALUE) > 0;
delete from dbo.SYSTEMINFO where keyword ='auto_renewal_email_failed_address_bcc' AND datalength(KEYWORDVALUE) > 0;
delete from dbo.SYSTEMINFO where keyword ='auto_renewal_email_successful_address_bcc' AND datalength(KEYWORDVALUE) > 0;
delete from dbo.SYSTEMINFO where keyword ='online_pending_customer_bcc' AND datalength(KEYWORDVALUE) > 0;

--Suspend production auto payments in case you need to use mstest.active that may cause errors send to mstest
UPDATE dbo.ARSCHEDULEHEADER SET SUSPEND_AUTO_PAY = -1;
UPDATE dbo.MEMBERSHIPS SET SUSPEND_AUTO_RENEWAL = -1;

--Disable scheduled reports
UPDATE dbo.REPORTDEFINITION SET RECIPIENT_ADDRESSES = '', ENABLE_EXPORT_TO_FTP = 0, SEND_CONFIRMATION_EMAIL = 0;

--Delete email and message tasks
delete dbo.BULKEMAILTASKS;
delete dbo.BULKEMAILATTACHMENTS;
delete dbo.BULKEMAILACKNOWLEDGEMENTS;
delete dbo.BULKEMAILRECIPIENTS;
delete dbo.OPTOUTHISTORY;
delete dbo.NEWSLETTER_OFFER_ORDER_PRODUCTS;
delete dbo.NEWSLETTER_OFFER_ORDERS;
delete dbo.CUSTOMER_SUBSCRIPTIONLIST;
delete dbo.MESSAGEQUEUES;
delete dbo.MESSAGES;
delete dbo.GROSSPAYEXPORTBATCHES;
delete dbo.ICVERIFYLOG;
delete dbo.REPORTDEFINITIONOVERRIDES;
delete dbo.REPORT_DEFINITION_TIME;

--Update credit card processor host address to localdemo
UPDATE dbo.SYSTEM SET VERISIGNHOSTADDRESS = 'localdemo';
UPDATE dbo.SYSTEM_USERS SET PASSWORD ='safari' WHERE USERNAME <> 'acmcuiuser';

--Disable akamai for local restore
--UPDATE dbo.SYSTEMINFO SET KEYWORDVALUE ='false' WHERE KEYWORD like 'use_akamai';

--Disable schedule load customer function
UPDATE dbo.SCHEDULED_LOAD_CUSTOMER SET SCHEDULE_FREQUENCY = 0;

--Clear skylogix configuration
DELETE FROM dbo.SYSTEMINFO WHERE KEYWORD in ('enable_run_skylogix_export', 'skylogix_client_id', 'skylogix_user_name', 'skylogix_user_password');

--Disable Outgoing Email (Admin > System Settings > Configuration - Internet Staff)
IF EXISTS(SELECT * FROM dbo.SYSTEMINFO WHERE KEYWORD = 'disable_outgoing_email') BEGIN
	UPDATE dbo.SYSTEMINFO SET KEYWORDVALUE = 'true' WHERE KEYWORD = 'disable_outgoing_email' and cast(KEYWORDVALUE as varchar(5)) = 'false';
END
ELSE BEGIN
	INSERT INTO dbo.SYSTEMINFO (KEYWORD, KEYWORDVALUE) VALUES ('disable_outgoing_email', 'true');
END

--Enable cache control on test sites
IF EXISTS(SELECT * FROM dbo.SYSTEMINFO WHERE KEYWORD = 'enable_cache_control_for_non_prod_site') BEGIN
	UPDATE dbo.SYSTEMINFO SET KEYWORDVALUE = 'true' WHERE KEYWORD = 'enable_cache_control_for_non_prod_site' and cast(KEYWORDVALUE as varchar(5)) = 'false';
END
ELSE BEGIN
	INSERT INTO dbo.SYSTEMINFO (KEYWORD, KEYWORDVALUE) VALUES ('enable_cache_control_for_non_prod_site', 'true');
END





if not exists (select keyword from systeminfo where keyword = 'is_load_test_system') 
	begin
		insert into systeminfo (keyword,keywordvalue) values ('is_load_test_system','true')
	end
	
	
	
update systeminfo set keywordvalue = 'false'
where keyword = 'force_email_as_login_name'


update [CUSTOMQUESTIONS] set required = 0 where required = -1

update systeminfo set keywordvalue = '/opt/active/ActiveNet/perf/SQLBACKUPS/perf01' where keyword = 'full_backup_unc'
update systeminfo set keywordvalue = 'W:\perf\SQLBACKUPS\perf01' where keyword = 'full_backup_unc_remote'
update systeminfo set keywordvalue = 'X:\perf01' where keyword = 'image_storage_path'
update systeminfo set keywordvalue = '/opt/active/data/an_filedata/perf01' where keyword = 'image_storage_path_local'
update systeminfo set keywordvalue = '/perf01/jreport/' where keyword = 'jreport_jsp_path'

select * from systeminfo where keyword in ('full_backup_unc','full_backup_unc_remote','image_storage_path','image_storage_path_local','jreport_jsp_path')



if not exists (select keywordvalue from systeminfo where KEYWORD = 'new_cui_url')
BEGIN
    insert into systeminfo (KEYWORD,KEYWORDVALUE) VALUES ('new_cui_url','https://ancperf.apm.activecommunities.com')
END
else
BEGIN
    update systeminfo set KEYWORDVALUE = 'https://ancperf.apm.activecommunities.com' where KEYWORD = 'new_cui_url'
END




if not exists (select * from systeminfo where keyword = 'enable_ignite_monitor')
	BEGIN
		insert into  systeminfo (KEYWORD,KEYWORDVALUE) values ('enable_ignite_monitor', 'false')
	END
else 
	BEGIN
		update systeminfo set KEYWORDVALUE = 'false' where KEYWORD = 'enable_ignite_monitor'
	END	

select * from systeminfo where keyword = 'enable_ignite_monitor'