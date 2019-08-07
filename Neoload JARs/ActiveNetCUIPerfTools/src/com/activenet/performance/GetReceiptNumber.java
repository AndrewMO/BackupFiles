
import org.apache.poi.xssf.usermodel.XSSFRow;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.*;

public class GetReceiptNumber {

    String ReceiptNumberExcelFile = "C:\\ajia\\AutoNumberCheck.xlsx";

//    String ReceiptNumberExcelFile = "D:\\Work\\AutoNumberCheck.xlsx";


    public void PutReceiptNumberIntoExcel(String timeStampMS, String receiptNumber){
        try {
            FileInputStream inp = new FileInputStream(new File("C:\\ajia\\AutoNumberCheck.xlsx"));  //获取已有文件
            XSSFWorkbook wb = new XSSFWorkbook(inp);
            XSSFSheet sheet = wb.getSheetAt(0);
            XSSFRow row = sheet.getRow(0);
            System.out.println(sheet.getLastRowNum()+" "+row.getLastCellNum());  //分别得到最后一行的行号，和一条记录的最后一个单元格


            FileOutputStream out=new FileOutputStream(new File("C:\\ajia\\AutoNumberCheck.xlsx"));  //向d://test.xls中写数据
            row=sheet.createRow((int)(sheet.getLastRowNum()+1)); //在现有行号后追加数据
            row.createCell(0).setCellValue(timeStampMS); //设置第一个（从0开始）单元格的数据
            row.createCell(1).setCellValue(receiptNumber); //设置第二个（从0开始）单元格的数据


            out.flush();
            wb.write(out);
            out.close();
            System.out.println(row.getPhysicalNumberOfCells()+" "+row.getLastCellNum());

        } catch (Exception e) {
            e.printStackTrace();
        }
        System.out.println("ok");



    }




    public static void main(String[] args) {
        GetReceiptNumber GRN = new GetReceiptNumber();

        String timeStampMS = "123";
        String receiptNumber = "1755610.001";

        GRN.PutReceiptNumberIntoExcel(timeStampMS, receiptNumber);

    }

}
