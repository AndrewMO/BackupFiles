package com.active.hpsperf;

import org.dom4j.Document;
import org.dom4j.Element;

public class PaymentResponse {
	public String Message = null;
	public String OtherFields = null;
	public String AuthorizationNumber = null;
	public String WalletId = null;

	public PaymentResponse(String response) {
		
		Document responseDoc = Request.loadXmlFromString(response);
		Element rootElement = responseDoc.getRootElement();
		Message = rootElement.elementText("Message");
		OtherFields = rootElement.elementText("OtherFields");
		AuthorizationNumber = rootElement.elementText("AuthorizationNumber");
		WalletId = rootElement.element("CardInfo").elementText("WalletId");
	}

}
