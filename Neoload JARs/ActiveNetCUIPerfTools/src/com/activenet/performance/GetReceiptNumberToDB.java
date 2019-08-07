package com.activenet.performance;

import java.sql.*;

public class GetReceiptNumberToDB {

    String connectionUrl = "jdbc:sqlserver://dev-neoload-01w.dev.activenetwork.com;database=ActiveNetPerformance;";
    String username = "recware";
    String password = "safari";

    // Mark the customerId as used
    public void updateReceiptNumber(String timeStampMS, String receiptNumber) throws ClassNotFoundException {
        Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
        String sql = "insert into AutoNumberVerify (timeStampMS, receiptNumber) values ("  +  timeStampMS + ", " + receiptNumber + " )";
        runSQL(sql);
    }

    void runSQL(String sql) {

        try {
            Connection con = DriverManager.getConnection(connectionUrl,
                    username, password);

            Statement smt = con.createStatement();
            smt.execute(sql);

            smt.close();
            con.close();

        } catch (Exception e) {
            e.printStackTrace();
        }

    }


}
