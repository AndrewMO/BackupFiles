
 -- Date range for queries
DECLARE @periodStartDate DATE = '2020-MAR-01';
DECLARE @periodEndDate DATE = CAST(GETDATE() as DATE); -- end date = EOD yesterday

SET NOCOUNT ON
SET QUOTED_IDENTIFIER ON
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED

-- Get "internet" system user id so can filter out from transactions
DECLARE @internetSiteId int = (select internetsite_id from dbo.system );
DECLARE @internetProfileId int = (select profile_id from dbo.profiles where name='Internet Profile')
DECLARE @internetUserId int = (select top (1) systemuser_id FROM dbo.system_users WHERE profile_id = @internetProfileId AND site_id = @internetSiteId order by systemuser_id);
 -- Get auto payments / renewals system user
DECLARE @autoPaymentsUserId int = (select cast(keywordvalue as int) from dbo.systeminfo where keyword='membership_auto_renewal_sys_user')

/**********************************************************************************
    System User Statistics 
***********************************************************************************
*/

 -- Query active system users for period (i.e. users that have logged on during period)
;with userLogonStats as (
    SELECT systemuser_id, max(logontime) AS lastLogon
    FROM dbo.SYSTEMUSAGELOG 
    WHERE SYSTEMUSER_ID > 0 AND SESSION_ID <> '_ServletUser' 
    AND LOGONTIME between @periodStartDate and @periodEndDate
    GROUP BY systemuser_id 
),
userStats as (
    SELECT su.SYSTEMUSER_ID,su.RETIRED, case when s.lastLogon is null then 0 else -1 end as isActiveSystemUser
        FROM dbo.SYSTEM_USERS su 
        LEFT OUTER JOIN userLogonStats s on su.SYSTEMUSER_ID = s.SYSTEMUSER_ID 
        WHERE ISNULL(su.ACTIVENET_SITES_USER_ID, 0) = 0  -- Filter out Active Network Portal users
        AND su.SYSTEMUSER_ID not in (@internetUserId, @autoPaymentsUserId)
)
SELECT sum(case when isActiveSystemUser = 0 then 0 else 1 end) as [Total Users Logged On During Period],
       count(SYSTEMUSER_ID) as [Total Sys Users], 
       sum(case when retired = 0 then 0 else 1 end) as [Num Retired Sys Users], 
       @periodStartDate as [Start Date], DATEADD(day, -1, @periodEndDate) as [End Date]
    FROM userStats 

 -- Query daily (approximate) maximum number of concurrent logged on users

;with AUIUserSessions as (
    SELECT CAST(LOGONTIME as date) as sessionDate,
           DATEPART(hh, LOGONTIME) as sessionLogonHour, 
           DATEPART(hh, CASE WHEN LOGGED_OUT > LOGONTIME THEN LOGGED_OUT 
                             WHEN TIMED_OUT > LOGONTIME THEN TIMED_OUT 
                             WHEN LOGINEXPIRATION > LOGONTIME THEN LOGINEXPIRATION
                             ELSE DATEADD(HOUR, 1, LOGONTIME)
                             END) as sessionLogoffHour,
           CAST(CASE WHEN LOGGED_OUT > LOGONTIME THEN LOGGED_OUT 
                             WHEN TIMED_OUT > LOGONTIME THEN TIMED_OUT 
                             WHEN LOGINEXPIRATION > LOGONTIME THEN LOGINEXPIRATION
                             ELSE DATEADD(HOUR, 1, LOGONTIME)
                             END as date) as sessionEndDate
        FROM dbo.SYSTEMUSAGELOG with (nolock) 
        WHERE SYSTEMUSER_ID > 0 AND SESSION_ID <> '_ServletUser' and SYSTEMUSER_ID NOT IN (@internetUserId, @autoPaymentsUserId)
            AND LOGONTIME BETWEEN @periodStartDate and @periodEndDate 
),
sessionHourBreakdown as (
    SELECT 0 as hourOfDay, COUNT(*) as numLoggedOn, sessionDate FROM AUIUserSessions WHERE sessionLogonHour < 1 AND sessionLogoffHour >= 0 GROUP BY sessionDate 
    UNION ALL 
    SELECT 1 as hourOfDay, COUNT(*) as numLoggedOn, sessionDate FROM AUIUserSessions WHERE sessionLogonHour < 2 AND sessionLogoffHour >= 1 GROUP BY sessionDate 
    UNION ALL 
    SELECT 2 as hourOfDay, COUNT(*) as numLoggedOn, sessionDate FROM AUIUserSessions WHERE sessionLogonHour < 3 AND sessionLogoffHour >= 2 GROUP BY sessionDate 
    UNION ALL 
    SELECT 3 as hourOfDay, COUNT(*) as numLoggedOn, sessionDate FROM AUIUserSessions WHERE sessionLogonHour < 4 AND sessionLogoffHour >= 3 GROUP BY sessionDate 
    UNION ALL 
    SELECT 4 as hourOfDay, COUNT(*) as numLoggedOn, sessionDate FROM AUIUserSessions WHERE sessionLogonHour < 5 AND sessionLogoffHour >= 4 GROUP BY sessionDate 
    UNION ALL 
    SELECT 5 as hourOfDay, COUNT(*) as numLoggedOn, sessionDate FROM AUIUserSessions WHERE sessionLogonHour < 6 AND sessionLogoffHour >= 5 GROUP BY sessionDate 
    UNION ALL 
    SELECT 6 as hourOfDay, COUNT(*) as numLoggedOn, sessionDate FROM AUIUserSessions WHERE sessionLogonHour < 7 AND sessionLogoffHour >= 6 GROUP BY sessionDate 
    UNION ALL 
    SELECT 7 as hourOfDay, COUNT(*) as numLoggedOn, sessionDate FROM AUIUserSessions WHERE sessionLogonHour < 8 AND sessionLogoffHour >= 7 GROUP BY sessionDate 
    UNION ALL 
    SELECT 8 as hourOfDay, COUNT(*) as numLoggedOn, sessionDate FROM AUIUserSessions WHERE sessionLogonHour < 9 AND sessionLogoffHour >= 8 GROUP BY sessionDate 
    UNION ALL 
    SELECT 9 as hourOfDay, COUNT(*) as numLoggedOn, sessionDate FROM AUIUserSessions WHERE sessionLogonHour < 10 AND sessionLogoffHour >= 9 GROUP BY sessionDate 
    UNION ALL 
    SELECT 10 as hourOfDay, COUNT(*) as numLoggedOn, sessionDate FROM AUIUserSessions WHERE sessionLogonHour < 11 AND sessionLogoffHour >= 10 GROUP BY sessionDate 
    UNION ALL 
    SELECT 11 as hourOfDay, COUNT(*) as numLoggedOn, sessionDate FROM AUIUserSessions WHERE sessionLogonHour < 12 AND sessionLogoffHour >= 11 GROUP BY sessionDate 
    UNION ALL 
    SELECT 12 as hourOfDay, COUNT(*) as numLoggedOn, sessionDate FROM AUIUserSessions WHERE sessionLogonHour < 13 AND sessionLogoffHour >= 12 GROUP BY sessionDate 
    UNION ALL 
    SELECT 13 as hourOfDay, COUNT(*) as numLoggedOn, sessionDate FROM AUIUserSessions WHERE sessionLogonHour < 14 AND sessionLogoffHour >= 13 GROUP BY sessionDate 
    UNION ALL 
    SELECT 14 as hourOfDay, COUNT(*) as numLoggedOn, sessionDate FROM AUIUserSessions WHERE sessionLogonHour < 15 AND sessionLogoffHour >= 14 GROUP BY sessionDate 
    UNION ALL 
    SELECT 15 as hourOfDay, COUNT(*) as numLoggedOn, sessionDate FROM AUIUserSessions WHERE sessionLogonHour < 16 AND sessionLogoffHour >= 15 GROUP BY sessionDate 
    UNION ALL 
    SELECT 16 as hourOfDay, COUNT(*) as numLoggedOn, sessionDate FROM AUIUserSessions WHERE sessionLogonHour < 17 AND sessionLogoffHour >= 16 GROUP BY sessionDate 
    UNION ALL 
    SELECT 17 as hourOfDay, COUNT(*) as numLoggedOn, sessionDate FROM AUIUserSessions WHERE sessionLogonHour < 18 AND sessionLogoffHour >= 17 GROUP BY sessionDate 
    UNION ALL 
    SELECT 18 as hourOfDay, COUNT(*) as numLoggedOn, sessionDate FROM AUIUserSessions WHERE sessionLogonHour < 19 AND sessionLogoffHour >= 18 GROUP BY sessionDate 
    UNION ALL 
    SELECT 19 as hourOfDay, COUNT(*) as numLoggedOn, sessionDate FROM AUIUserSessions WHERE sessionLogonHour < 20 AND sessionLogoffHour >= 19 GROUP BY sessionDate 
    UNION ALL 
    SELECT 20 as hourOfDay, COUNT(*) as numLoggedOn, sessionDate FROM AUIUserSessions WHERE sessionLogonHour < 21 AND sessionLogoffHour >= 20 GROUP BY sessionDate 
    UNION ALL 
    SELECT 21 as hourOfDay, COUNT(*) as numLoggedOn, sessionDate FROM AUIUserSessions WHERE sessionLogonHour < 22 AND sessionLogoffHour >= 21 GROUP BY sessionDate 
    UNION ALL 
    SELECT 22 as hourOfDay, COUNT(*) as numLoggedOn, sessionDate FROM AUIUserSessions WHERE sessionLogonHour < 23 AND sessionLogoffHour >= 22 GROUP BY sessionDate 
    UNION ALL 
    SELECT 23 as hourOfDay, COUNT(*) as numLoggedOn, sessionDate FROM AUIUserSessions WHERE sessionLogonHour < 23 AND (sessionLogoffHour > 23 or sessionEndDate > sessionDate) GROUP BY sessionDate 
),
AUISessionStats as (
    SELECT sessionDate, MAX(numLoggedOn) as maxConcurrentlyLoggedOn, AVG(numLoggedOn) as avgConcurrentlyLoggedOn 
    FROM sessionHourBreakdown 
    GROUP BY sessionDate
)
SELECT sessionDate as [Session Date],
       maxConcurrentlyLoggedOn as [Max Concurrently Logged On Per Hour],
       avgConcurrentlyLoggedOn as [Avg Concurrently Logged On Per Hour], 
       DATENAME(DW, sessionDate) as [Day of Wk] 
FROM AUISessionStats 
ORDER BY sessionDate 

/**********************************************************************************

    AUI Transaction Statistics 

***********************************************************************************
*/

;with AUITransactionData as (
    SELECT TRANSACTION_ID, 
            -- Fix up some subsystem code values
           case when tr.subsystem_code = 8 then 
                case when tr.transactiontype in (51, 52, 83) then 8001 -- gift card transactions 
                        else tr.subsystem_code 
                        end
            else tr.subsystem_code 
            end as subsystemCode  
    FROM dbo.TRANSACTIONS tr 
    WHERE datestamp between @periodStartDate and @periodEndDate 
    AND systemuser_id not in (@autoPaymentsUserId, @internetUserId)  
    AND site_id not in (@internetSiteId) 
    AND transactiontype not in (53) -- transaction fee
),
AUITransactionDataFiltered as (
    SELECT f.subsystemCode, CAST(tr.DATESTAMP as date) AS transactionDate, DATEPART(hh, tr.DATESTAMP) AS transactionHourOfDay, COUNT(*) as numTransactionsByHour 
    FROM AUITransactionData f JOIN dbo.TRANSACTIONS tr on f.TRANSACTION_ID = tr.TRANSACTION_ID 
    GROUP BY f.subsystemCode, CAST(tr.DATESTAMP as date), DATEPART(hh, tr.DATESTAMP)
),
AUITransactionStats as (
    SELECT subsystemCode, transactionDate, MAX(numTransactionsByHour) as maxTransactionsPerHour, AVG(numTransactionsByHour) as avgTransactionsPerHour
    FROM AUITransactionDataFiltered td 
    GROUP BY transactionDate, subsystemCode 
)
SELECT transactionDate as [Transaction Date],
    case when subsystemCode = 0 then 'None'
         when subsystemCode = 1 then 'Payment on plan'
         when subsystemCode = 2 then 'Activity Transactions'
         when subsystemCode = 3 then 'POS Transactions'
         when subsystemCode = 4 then 'Reservation Transactions'
         when subsystemCode = 5 then 'Membership Transactions'
         when subsystemCode = 6 then 'Flexreg Transactions'
         when subsystemCode = 7 then 'Donation Transactions'
         when subsystemCode = 8001 then 'Gift Card Transactions'
         when subsystemCode = 8 then 'Misc'
         else '???' 
         end as Module,
    maxTransactionsPerHour as [Max Trx Per Hour],
    avgTransactionsPerHour as [Avg Trx Per Hour],
    DATENAME(DW, transactionDate) as [Day of Wk]
FROM AUITransactionStats 
ORDER BY transactionDate, subsystemCode 

/****************************************************************************************

    AUI Report Statistics

 ***********************************************************************************
*/

;with AUIReportCountsByDayAndHour as (
    SELECT CAST(r.RECNETSTARTTIME as date) as reportDate, DATEPART(hh, r.RECNETSTARTTIME) as reportHourOfDay, COUNT(*) as numReportsByHour
        FROM dbo.RSERVERLOG r 
        LEFT OUTER JOIN dbo.SYSTEM_USERS su on r.SYSTEMUSER_ID = su.SYSTEMUSER_ID  
    WHERE ISNULL(su.ACTIVENET_SITES_USER_ID, 0) = 0  -- Filter out Active Network Portal users
    AND su.SYSTEMUSER_ID not in (@internetUserId) -- Filter out scheduled reports 
    AND r.RECNETSTARTTIME between @periodStartDate and @periodEndDate 
    GROUP BY CAST(r.RECNETSTARTTIME as date), DATEPART(hh, r.RECNETSTARTTIME)
),
AUIReportStats as (
    SELECT reportDate, MAX(numReportsByHour) as maxReportsPerHour, AVG(numReportsByHour) as avgReportsPerHour 
    FROM AUIReportCountsByDayAndHour 
    GROUP BY reportDate 
)   
SELECT reportDate as [Report Date],
       maxReportsPerHour as [Max Reports Per Hour],
       avgReportsPerHour as [Avg Reports Per Hour],
       DATENAME(DW, reportDate) as [Day of Wk]
FROM AUIReportStats 
ORDER BY reportDate 