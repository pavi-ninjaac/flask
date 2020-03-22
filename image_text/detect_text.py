import cv2
import pytesseract
def Detect_text(path):
    pytesseract.pytesseract.tesseract_cmd='E:\\tesseract\\installed_file\\tesseract.exe'
    
    img=cv2.imread(path,1)
    
    text=pytesseract.image_to_string(img)
    return text
    



