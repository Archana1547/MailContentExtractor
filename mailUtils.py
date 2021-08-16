from datetime import datetime, timedelta

import win32com
import pdfReader

class mailExtractorUtils:
    def connectToMail(self):
        outlook = win32com.client.Dispatch("Outlook.Application")
        mapi = outlook.GetNamespace("MAPI")
        inbox = mapi.GetDefaultFolder(5)
        messages = inbox.Items
        received_dt = datetime.now() - timedelta(days=1)
        received_dt = received_dt.strftime('%m/%d/%Y %H:%M %p')
        messages=messages.Restrict("[ReceivedTime] >= '" + received_dt + "'")
        return messages
       # messages = inbox.Items

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
           print("WHy")
           data="No attachments"
        return data

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



