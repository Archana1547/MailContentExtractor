import pdfplumber as pp
import pytesseract
from pdf2image import convert_from_path
from PIL import Image


class pdfUtils:

    # This method will convert scanned pdf into editable pdf and return its content
    def getScannedPdfConetnt(self,img):

        #pytesseract connects to tesseract module and perform ocr
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

        #this line will convert the pdf into image and through poppler we can render it
        images=convert_from_path(img,300,poppler_path=r'poppler-0.68.0_x86/poppler-0.68.0/bin')

        for i in range(len(images)):
            images[i].save('page' + str(i) + '.jpg', 'JPEG')
            text = (pytesseract.image_to_string(Image.open('page'+str(0)+'.jpg')))
            text = repr(text)
            text=text.replace("\\n","")
            return text


    #This method will extract text from pdfs
    def getNormalPdfContent(self,pdf):
        with pp.open(pdf) as pdf:
            page1=pdf.pages[0]
            return page1.extract_text()

    # This method will check which method to call from above 2
    # If the attachement contains sacnned pdf,it will return None when tried to read
    #otherwise it will return the text
    # 
    def readPDF(self,pdf):
        if self.getNormalPdfContent(pdf) is None:
            return self.getScannedPdfConetnt(pdf)
        else:
            return self.getScannedPdfConetnt(pdf)

        
        
        


