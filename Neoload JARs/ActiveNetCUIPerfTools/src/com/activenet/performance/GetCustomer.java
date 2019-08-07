package com.activenet.performance;

import java.sql.*;

public class GetCustomer {
	String connectionUrl = "jdbc:sqlserver://dev-neoload-01w.dev.activenetwork.com;database=ActiveNetPerformance;";
	String username = "recware";
	String password = "safari";

	// Get customerID randomly
	public String randomCustoemrID(String orgName)
			throws ClassNotFoundException {
		Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
		String sql = "select top 1 customer_id from " + orgName + " where used = 0 order by newid()";
		return getIdFromSQL(sql);

	}
	
	String getIdFromSQL(String sql) {
		String customerID = null;

		try {
			Connection con = DriverManager.getConnection(connectionUrl,
					username, password);
			Statement smt = con.createStatement();

			// Get customerID
			ResultSet result = smt.executeQuery(sql);
			result.next();
			customerID = result.getString(1);
			
			smt.close();
			con.close();

		} catch (Exception e) {
			e.printStackTrace();
		}
		return customerID;

	}
}
