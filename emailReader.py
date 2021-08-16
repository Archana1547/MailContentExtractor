import win32com.client
import os
import pdfReader
import mailUtils
import connection
import stdiomask

mailSer=mailUtils.mailExtractorUtils()
messages=mailSer.connectToMail()

bodyList=[]
aList=[]
contents={}
connection= connection.connectionDB()
for message in messages:
    attachment=message.attachments
    aData=mailSer.getAttachment(attachment)
    body=mailSer.getBody(message)
    """bodyList.append(body)
    aList.append(aData)"""
    contents={"attachment":aData,"body":body}
    coln=connection.getDB()
    coln.insert_one(contents)



#body=mailSer.getBody(connection)


