import pdfplumber as pp
import pytesseract
from pdf2image import convert_from_path
from PIL import Image


class pdfUtils:

    def getScannedPdfConetnt(self,img):
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        images=convert_from_path(img,300,poppler_path=r'poppler-0.68.0_x86/poppler-0.68.0/bin')
        for i in range(len(images)):
            images[i].save('page' + str(i) + '.jpg', 'JPEG')
            text = (pytesseract.image_to_string(Image.open('page'+str(0)+'.jpg')))
            text = repr(text)
            text=text.replace("\\n","")
            return text


    def getNormalPdfContent(self,pdf):
        with pp.open(pdf) as pdf:
            page1=pdf.pages[0]
            return page1.extract_text()


    def readPDF(self,pdf):
        if self.getNormalPdfContent(pdf) is None:
            return self.getScannedPdfConetnt(pdf)
        else:
            return self.getScannedPdfConetnt(pdf)



