package com.active.hpsperf;

import java.io.*;

import org.dom4j.*;
import org.dom4j.io.*;

/**
 * @author wran
 *
 */
public class Request {

	String prefixXML = "<?xml version=\"1.0\"?>";

	static Document loadXmlFromString(String XMLString) {
		XMLString = CipherCode.decrypt(XMLString);
		SAXReader reader = new SAXReader();
		Document doc;
		try {
			doc = reader.read(new StringReader(XMLString));
			return doc;
		} catch (DocumentException e) {
			e.printStackTrace();
		}
		return null;
	}


	/**
	 * @param amsCipherText
	 * @param Modulus
	 * @param paymentResponse
	 * @param RequestTicket
	 * @return Encrypted commit request
	 */
	public String getCommitRequest(String amsCipherText, String Modulus,
			String paymentResponse, String RequestTicket) {
		Document doc = loadXmlFromString(RawData.commitTransaction);
		Element rootElement = doc.getRootElement();

		PaymentResponse response = new PaymentResponse(paymentResponse);

		// Set Modulus
		rootElement.element("Modulus").setText(Modulus);

		// Set AMSCipherText
		rootElement.element("AMSCipherText").setText(amsCipherText);
		
		// Set RequestTicket
		rootElement.element("RequestTicket").setText(RequestTicket);

		// Set OtherFields
		rootElement.element("Result").element("OtherFields")
				.setText(response.OtherFields);

		// Set AuthorizationNumber
		rootElement.element("Result").element("AuthorizationNumber")
				.setText(response.AuthorizationNumber);
		
		// Set WalletId
		rootElement.element("Result").element("CardInfo").element("WalletId")
		.setText(response.WalletId);
		
		// Set RequestType
		rootElement.element("RequestType").setText("8");

		return CipherCode.encrypt(prefixXML + rootElement.asXML());
	}

	/**
	 * @param amsCipherText
	 * @param Modulus
	 * @param RequestTicket
	 * @return Encrypted payment request
	 */
	public String getPaymentRequest(String amsCipherText, String Modulus, String RequestTicket) {
		// Document doc = request.loadXmlFromFile();
		Document doc = loadXmlFromString(RawData.paymentRequest);
		Element rootElement = doc.getRootElement();

		// Set Modulus
		rootElement.element("Modulus").setText(Modulus);

		// Set AMSCipherText
		rootElement.element("AMSCipherText").setText(amsCipherText);
		
		// Set RequestTicket
		rootElement.element("RequestTicket").setText(RequestTicket);

		return CipherCode.encrypt(prefixXML + rootElement.asXML());

	}

}
