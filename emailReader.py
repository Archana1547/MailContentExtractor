import mailUtils
import connection


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
    
    # This will save attachments and bdy from the mail in a dictionary
    contents={"attachment":aData,"body":body}
    
    #This will get connection from the database and save the records accoringly
    coln=connection.getDB()
    coln.insert_one(contents)




