import java.sql.SQLException;

import com.activenet.performance.*;

public class test {

	public static void main(String[] args) throws ClassNotFoundException, SQLException {
	GetCustomer update =new GetCustomer();
	String id = update.randomCustoemrID("acm01vegasjetty");
	System.out.println(id);

	}
}
