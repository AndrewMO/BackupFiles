//GetRandomDate by Andrew
//random date range:2017-01-01~2017-12-31
var year =2017;

//Get random month number in [6,12]
var min =6 ;
var max = 12;
var random = Math.random();
var count = Math.floor(min+random*(max-min));
var month = count;
var monthforswitch = month;
if(month < 10)
{
    month ="0"+month;
}

logger.debug("Random month is:  "+month);

//Get random day number
switch(monthforswitch)
{
      case 7:
      case 8:
      case 10:
      case 12:
            var min = 1;
            var max = 31;
            var random = Math.random();
            var count = Math.floor(min+random*(max-min));
            var day = count;
            if(day < 10)
            {
                day ="0"+day;
            }
            logger.debug("Random day is:  "+day);
            break;
        case 6:
        case 9:
        case 11:
            var min = 1;
            var max = 30;
            var random = Math.random();
            var count = Math.floor(min+random*(max-min));
            var day = count;
            if(day < 10)
            {
                day ="0"+day;
            }
            logger.debug("Random day is:  "+day);
            break;
         default:
             logger.debug("Error Date inRandom Day");
             break;
        
}



var randomdate =""+year+"-"+month+"-"+day;

 logger.debug("RandomDate is :"+randomdate);

context.variableManager.setValue("Randomdate",randomdate);