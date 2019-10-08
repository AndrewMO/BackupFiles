// Generate random date between given range
// Wayne Ran
// August 27,2017 

// Set start & end date & random range
var startDate = new Date();
var endDate = new Date();
var rndDays = Math.round(Math.random()*26);
startDate.setFullYear(2016,9,1);
endDate.setFullYear(2017,9,1);

// Add random days to start date
startDate.setDate(startDate.getDate()+ rndDays);
endDate.setDate(endDate.getDate()+ rndDays);

// Format date
var startDate_month = startDate.getMonth()+1;
var startDate_day = startDate.getDate();

var endDate_month = endDate.getMonth()+1;
var endDate_day = endDate.getDate();

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