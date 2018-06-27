// Javascript skeleton.
// Edit and adapt to your needs.
// The documentation of the NeoLoad Javascript API
// is available in the appendix of the documentation.

var endDate = new Date();
//randomdays range 0~30

var randomDays =(Math.random()*30);
randomDays = Math.round(randomDays);

logger.debug("randomdays :"+randomDays);
endDate.setDate(endDate.getDate()-randomDays);
logger.debug("selectEndDate :"+endDate);

var startDate = new Date();
startDate.setDate(endDate.getDate()-365);
logger.debug("selectStartDate :"+startDate);

//generate StartDate and EndDate
var year_start = startDate.getFullYear();
var month_start = startDate.getMonth()+1;
var day_start = startDate.getDate();
logger.debug("StartDate"+year_start+","+month_start+","+day_start);

if(month_start<10){ 
	month_start = "0"+month_start;
} 
if(day_start<10){ 
	day_start = "0"+day_start;
}
var proDate_start = year_start + "-" + month_start + "-" + day_start;
logger.debug("StartDate :"+proDate_start);
context.variableManager.setValue("StartDate",proDate_start);

var year_end = endDate.getFullYear();
var month_end = endDate.getMonth()+1;
var day_end = endDate.getDate();
logger.debug("EndtDate"+year_end+","+month_end+","+day_end);

if(month_end<10){ 
	month_end = "0"+month_end;
} 
if(day_end<10){ 
	day_end = "0"+day_end;
}
var proDate_end = year_end + "-" + month_end + "-" + day_end;

logger.debug("EndDate :"+proDate_end);
context.variableManager.setValue("EndDate",proDate_end);