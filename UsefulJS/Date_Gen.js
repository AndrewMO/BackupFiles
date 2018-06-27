// Set start & end date & random range
var startDate =  new Date();
var endDate =  new Date();





//Generate randomdays[1,30]
var min = 1;
var max = 365;
var rndDays = Math.round(Math.random()*(max-min+1)+min);

startDate.setDate( startDate.getDate() - rndDays);
endDate.setDate( endDate.getDate() - rndDays + 30);

logger.debug("startDate = "+startDate);

logger.debug("endDate = "+endDate);

// Format date
var startDate_month = startDate.getMonth()+1;
var startDate_day = startDate.getDate();

logger.debug("startDate_month = "+startDate_month);
logger.debug("startDate_day = "+startDate_day);

var endDate_month = endDate.getMonth()+1;
var endDate_day = endDate.getDate();

logger.debug("endDate_month = "+endDate_month);
logger.debug("endDate_day = "+endDate_day);

function formatDate(monthOrDay)
{
	if (monthOrDay < 10) {
		return "0" + monthOrDay;
	} else {
		return monthOrDay;
	}
}

var startRange = startDate.getFullYear() + "-" + formatDate(startDate_month) + "-" + formatDate(startDate_day);
var endRange = endDate.getFullYear() + "-" + formatDate(endDate_month) + "-" + formatDate(endDate_day);

logger.debug("startRange = "+startRange);
logger.debug("endRange = "+endRange);

// Return value
context.variableManager.setValue("Start_Date",startRange);
context.variableManager.setValue("End_Date",endRange);