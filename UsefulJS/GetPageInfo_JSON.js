// Get Page Info
// Author: Andrew Jia
// Last modified date: Oct 12,2017

var response = context.variableManager.getValue("Response_Body");
if (response==null) {
        context.fail("Variable 'Response_Body' not found");
}
//logger.debug("Response_Body = " + response);

var responseJason = JSON.parse(response);
try{
    var maxpageNumber = JSON.stringify(responseJason.headers.page_info.total_page);
    //Inject the computed value in a runtime variable
    context.variableManager.setValue("MaxPageNumber",maxpageNumber);
}
catch(err)
{
    context.variableManager.setValue("MaxPageNumber","<NOT FOUND>");
}

logger.debug("maxpageNumber  = " + maxpageNumber);