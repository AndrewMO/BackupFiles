select mu.MEMBERSHIPUSAGE_ID,mu.MEMBERSHIP_ID,mu.CUSTOMER_ID,m.PACKAGE_ID, mu.TIMEUSED

from MEMBERSHIP_USAGES mu WITH(NOLOCK)

join CUSTOMERS c WITH(NOLOCK) on mu.CUSTOMER_ID = c.CUSTOMER_ID

left join MEMBERSHIPS m WITH(NOLOCK) on mu.MEMBERSHIP_ID = m.MEMBERSHIP_ID

where mu.AUTHORIZED = -1 and mu.VOIDEDBY = 0