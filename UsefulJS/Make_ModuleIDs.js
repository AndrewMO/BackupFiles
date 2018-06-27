// Javascript skeleton.
// Edit and adapt to your needs.
// The documentation of the NeoLoad Javascript API
// is available in the appendix of the documentation.

// Get variable value from VariableManager
var count = context.variableManager.getValue("ARSummary_ModuleID_ID_matchNr");
if (count==null) {
        context.fail("Variable 'ARSummary_ModuleID_ID' not found");
}

var Ids = "";

if (count > 0 ) {
  for (var i=1; i<=count; i++)
    {
      Ids = Ids + "\"" + context.variableManager.getValue("ARSummary_ModuleID_ID_" + i) +"\"" +",";
    }

  Ids = Ids.slice(0,-1);
  logger.debug("Ids:" + Ids);
}


var IdList = Ids;
var IdListEncode = IdList;
var IdListGetLink = IdList

// Generate ID list
IdList = IdList.replace(/"/g,"");
IdList = IdList.replace(/,/g,"&ModuleID=");
IdList = "ModuleID=" + IdList;
logger.debug("IDs:" + IdList);

// Generate Encoded ID list
IdListEncode = IdListEncode.replace(/"/g,"");
IdListEncode = IdListEncode.replace(/,/g,"%2C%20");
logger.debug("IdListEncode:" +IdListEncode);

// Generate Get request  link ID list
IdListGetLink = IdListGetLink.replace(/"/g,"");
IdListGetLink = IdListGetLink.replace(/,/g,"%2C+");
logger.debug("IdListGetLink:" +IdListGetLink);


context.variableManager.setValue("ARSummary_ModuleID_IDs",Ids );
context.variableManager.setValue("ARSummary_ModuleID_List",IdList );
context.variableManager.setValue("ARSummary_ModuleID_Encode",IdListEncode );
context.variableManager.setValue("ARSummary_ModuleID_GetLink",IdListGetLink );