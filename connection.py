from pymongo import MongoClient
import xml.etree.ElementTree as ET
import os

#connectionURL=os.environ.get('connection_string')
#print(os.environ.get('password'))
#print(os.getenv('password'))

class connectionDB:
   """def getURI(self,file):
        tree = ET.parse(file)
        rootTag=tree.getroot()
        return rootTag[0].text"""
   def getDB(self):
       connectionString="<connection String>"   #self.getURI("Properties.xml")
       client = MongoClient(connectionString)
       db=client['ECEx']
       coln=db['contents']
       return coln

