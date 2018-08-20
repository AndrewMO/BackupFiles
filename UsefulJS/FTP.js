// Initialisation

myFTPClient =new Packages.org.apache.commons.net.ftp.FTPClient(); myFTPClient.connect("servername"); myFTPClient.login("username","password"); logger.debug(myFTPClient.getReplyCode()+" "+myFTPClient.getReplyString());

 

//Command PWD

 

myFTPClient.printWorkingDirectory(); logger.debug(myFTPClient.getReplyCode()+" "+myFTPClient.getReplyString());

 

//Create a new folder with MKDIR command

 

myFTPClient.makeDirectory("FTPNeoload"); logger.debug(myFTPClient.getReplyCode()+" "+myFTPClient.getReplyString());



//Command LIST

 

engine =myFTPClient.initiateListParsing("/");

while (engine.hasNext())

{

file = engine.getNext(5);

logger.debug(file[0].getName());

}

 

//Use of the GET method

 

var writer = new java.io.FileOutputStream("c:\\Temp\\MyFile.zip",true);

myFTPClient.retrieveFile("MyFile.zip",writer);

writer.close();

logger.debug(myFTPClient.getReplyCode()+" "+myFTPClient.getReplyString());

 

//Use of the PUT method

 

var reader = new java.io.FileInputStream("c:\\Temp\\myfile.xps"); myFTPClient.storeFile("myfile.xps",reader);

reader.close();

logger.debug(myFTPClient.getReplyCode()+" "+myFTPClient.getReplyString());

myFTPClient.logout();

myFTPClient.disconnect();