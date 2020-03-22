from PIL import Image
import io
from pytesseract import image_to_string
import re


def imageToText(bytesArray):
    image = Image.open(io.BytesIO(bytesArray))
    text = image_to_string(image, lang='rus')
    text = re.split('\s',text)
    searchWords = []
    for word in text:
        if len(word)>3:
            searchWords.append(word)
            
    return searchWords