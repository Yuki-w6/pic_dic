import pytesseract
from PIL import Image

str_img = Image.open('ocr_test/string.png')
str = pytesseract.image_to_string(str_img)
print(str)
