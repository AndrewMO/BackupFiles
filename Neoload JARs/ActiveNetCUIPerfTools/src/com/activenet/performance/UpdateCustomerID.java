package com.activenet.performance;

import java.sql.*;

public class UpdateCustomerID {
	String connectionUrl = "jdbc:sqlserver://dev-neoload-01w.dev.activenetwork.com;database=ActiveNetPerformance;";
	String username = "recware";
	String password = "safari";

	// Mark the customerId as used
	public void updateUsedCustomerID(String orgName, String customerID)
			throws ClassNotFoundException {
		Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
		String sql = "update " + orgName + " set used = 1 where customer_id = "
				+ customerID;
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
