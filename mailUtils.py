from datetime import datetime, timedelta

import win32com
import pdfReader

class mailExtractorUtils:

    #This method will connect the application to outlook
    def connectToMail(self):
        outlook = win32com.client.Dispatch("Outlook.Application")

        #mapi is Messaging API,it will let us to connect to outlook and give access to mails
        mapi = outlook.GetNamespace("MAPI")

        #For every folder, a distinct number is given, through that number we can acces
        # all the mails in of the folder associated with it
        # 5 is for Sent Items, 6 is for Inbox and so on
        #Below line will fetch the folder
        inbox = mapi.GetDefaultFolder(6)

        #This will fetch emails in that folder
        messages = inbox.Items

        #This will impose a Filter on the mails which are fetched
        #Only those mails which are received in past 24 hrs will be fetched
        received_dt = datetime.now() - timedelta(days=1)
        received_dt = received_dt.strftime('%m/%d/%Y %H:%M %p')
        messages=messages.Restrict("[ReceivedTime] >= '" + received_dt + "'")
        return messages


    #This method will extrct attachments of the mails
    def getAttachment(self,attachments):
        pdfUtil=pdfReader.pdfUtils()
        data=""
        #print(attachments.Count)
        if (attachments.Count >= 1):

            for attachment in attachments:

                filename=str(attachment.FileName)

                if filename.endswith(".pdf")==True:
                    data=pdfUtil.readPDF(attachment.FileName) # attachment.FileName
                    """elif filename.endswith(".jpg")==True | filename.endswith(".jpeg")==True | filename.endswith(".png")==True :
                        data=filename"""
                else:
                    data=filename #  pdfUtil.getOtherFormatContent(attachment.FileName)

        else:
           data="No attachments"
        return data

    #THis method will fetch body of the mail
    def getBody(self,message):
        #messages = messages.Items
        body=message.Body
        return body

"""        record={}
       # print(message)
        attachment = message.attachments
        print(attachment)
        attachmentData= self.getAttachment(attachment)
        body= self.getBody(message)
        record={"body":body,"a":attachmentData}
        return record"""




