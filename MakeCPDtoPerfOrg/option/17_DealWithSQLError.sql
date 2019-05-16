use acm01vegasjetty


--find team id
select pending_team_owner, * from teams where pending_team_owner is not null  and pending_team_owner <>　''



--update transactions table with teamID 
update [TRANSACTIONS] set team_id = null
where team_id = 25948 