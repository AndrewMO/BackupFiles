use acm01vegasjetty

-- Allow customer login as Customer_ID
update systeminfo set keywordvalue = 'false'
where keyword = 'force_email_as_login_name'