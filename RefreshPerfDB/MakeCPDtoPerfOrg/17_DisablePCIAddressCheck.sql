use ACM01vegasJetty



IF not exists (select keywordvalue from SYSTEMINFO where KEYWORD = 'disable_pci_checkout_service_url_validation')
BEGIN
    insert into SYSTEMINFO (KEYWORD, KEYWORDVALUE) values ('disable_pci_checkout_service_url_validation', 'true')
END
ELSE
BEGIN
    update systeminfo set KEYWORDVALUE = 'true' where KEYWORD = 'disable_pci_checkout_service_url_validation'
END