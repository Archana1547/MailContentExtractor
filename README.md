

# ContentExtractor
To extract attachments (pdf  contents) and body from mail 


Hi,

This project will connect to outlook and save the attachments and body of the mail in the database
This is specificlly implemented for reading and saving scanned pdfs,scanned pdfs are the one whose text is not selectable
Database Used in this project is MongoDB Atlas, a cloud based database which can be acessible from anywhere
One need to provide the credetianls for connecting to database in connection.py file, etiher create a prperties.xml file and access it's element from the connection.py file
Since this was meant to be for pdfs only,I haven't provided the methods for other formats attatchment, but if you want to implement it , 
it will be similar to the getNormalPdfContent of pdfReader.py files
For execution,execute the emailReader.py file

ThankYou 
