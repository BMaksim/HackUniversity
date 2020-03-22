import psycopg2
import pandas as pd
from pytesseract import image_to_string
from PIL import Image

text = image_to_string(Image.open('./2.jpg'), lang='rus')
print(text)