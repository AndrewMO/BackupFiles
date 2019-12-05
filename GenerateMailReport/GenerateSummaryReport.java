import java.io.*;
import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class GenerateSummaryReport {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		
		File reportFile = new File("C:/Program Files (x86)/Jenkins/workspace/ANDailyPerfTest/neoload-report/report_files/summary.html");
		File versionFile = new File("C:/Program Files (x86)/Jenkins/workspace/ANDailyPerfTest/version.html");
		String reportFile_origian = "<div align=\"center\">";
		String versionFile_origian = "";
        
		//读取Neoload的Summary.Html文件
		if(reportFile.isFile() && reportFile.exists()) {
			InputStreamReader read = new InputStreamReader(new FileInputStream(reportFile));
			BufferedReader bufferedReader = new BufferedReader(read);
			
	        String lineTxt = null;
	        while ((lineTxt = bufferedReader.readLine()) != null) {
	        	
	        	reportFile_origian+= lineTxt;
	               
	        }
	        reportFile_origian = reportFile_origian + "</div>";
	        read.close();
	       } else {
            System.out.println("Report file not found");
           }
		
		//读取CURL抓取的version.Html文件
		if(versionFile.isFile() && versionFile.exists()) {
			InputStreamReader read = new InputStreamReader(new FileInputStream(versionFile));
			BufferedReader bufferedReader = new BufferedReader(read);
	        String lineTxt = null;
	        while ((lineTxt = bufferedReader.readLine()) != null) {
	        	
	        	versionFile_origian+= lineTxt;
	               
	        }
	        read.close();
	       } else {
	            System.out.println("Version file not found");
	      }
		
		
		
		
	        

	      //取出Summary Report部分
	        String regularString_Report = "<table style=\"border: 0\" class=\"statistics_summary_template\">(.*?)</table>";
	        String summaryReportTable = getStrings(reportFile_origian,regularString_Report);
	        
	      
	        
	      //去掉图片的url
	        String replaceRegularStatement_Report = "<td><img src=(.*?)style=\"vertical-align: middle;\"></td>";
	        String textReportTable = replace(summaryReportTable,replaceRegularStatement_Report);
	        

	        //添加html格式
	        String prefix_Report = "<div align=\"center\">\r\n" + "<table style=\"border: 0\" class=\"statistics_summary_template\">\r\n";
	        String suffix_Report = "\r\n" + "</table>\r\n" + "</div>";
	        
	        String newSummaryTable = prefix_Report + textReportTable + suffix_Report;
	        
	        
	        
	        
		     //取出Version信息
	        String regularString_Version = "<div style=\"margin:100px;font-size:xx-large\">(.*?)</div>";
	        
	        
	        String summaryTable = getStrings(versionFile_origian,regularString_Version);
	        
		   //去掉server信息
	        String replaceRegularStatement_Version = "<strong>Current server:&nbsp;ANWSSTGACM0104</strong>";
	        
	        String textTable_Version = replace(summaryTable,replaceRegularStatement_Version);
	        
	        //添加html格式
	        
	        String prefix_Version = "<div align=\"center\";font-size:xx-large\">"+"\r\n";
	        String suffix_Version = "\r\n"+"</div>";
	        
	        String finalReport =  prefix_Version + textTable_Version + suffix_Version + "\r\n" + "</br>" + "</br>" + newSummaryTable;
	        
	        
	        
	        //输出编辑后的Summary文件
			File f1 = new File("C:/Program Files (x86)/Jenkins/workspace/ANDailyPerfTest/Report_export.html");
			FileWriter fw = new FileWriter(f1);
			fw.write(finalReport);
			fw.close();

	        

		

}
	
	
	
	
    private static String getStrings(String str, String RegularString) {
        Pattern p = Pattern.compile(RegularString);
        Matcher m = p.matcher(str);
        ArrayList<String> strs = new ArrayList<String>();
        while (m.find()) {
            strs.add(m.group(1));            
        } 
//        for (String s : strs){
//            System.out.println(s);
//        } 
        
        
        String summarytable = strs.toString().replaceAll("\\[|\\]", "");
        
        return summarytable;
    }
    
    
    private static String replace(String str,String replaceRegularStatement) {
        
        str = str.replaceAll(replaceRegularStatement, " ");        
        
        return str;
    }
    

}
