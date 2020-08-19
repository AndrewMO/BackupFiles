// Generate random date between given range
// Andrew Jia
// July 31,2019 

// Set start & end date & random range
var endDate = new Date();

//random days
var rndDays = Math.round(Math.random()*180);
rndDays = Math.round(rndDays);
logger.debug("randomdays :"+rndDays);
endDate.setUTCDate(endDate.getUTCDate()-rndDays);

logger.debug("selectEndDate :"+endDate);

var endDate_month = endDate.getUTCMonth()+1;
var endDate_day = endDate.getUTCDate();

var endRange = endDate.getUTCFullYear() + "-" + formatDate(endDate_month) + "-" + formatDate(endDate_day);

//set startDate
var startDate = endDate;
startDate.setUTCDate(endDate.getUTCDate()-90);


logger.debug("selectStartDate :"+startDate);


// Format date
var startDate_month = startDate.getUTCMonth()+1;
var startDate_day = startDate.getUTCDate();



function formatDate(monthOrDay)
{
	if (monthOrDay < 10) {
		return "0" + monthOrDay;
	} else {
		return monthOrDay;
	}
}

var startRange = startDate.getUTCFullYear() + "-" + formatDate(startDate_month) + "-" + formatDate(startDate_day);


logger.debug("startRange = "+startRange);
logger.debug("endRange = "+endRange);

// Return value
context.variableManager.setValue("Start_Date",startRange);
context.variableManager.setValue("End_Date",endRange);