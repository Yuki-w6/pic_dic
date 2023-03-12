import pytesseract
from PIL import Image

str_img = Image.open('ocr_test/string.png')
str = pytesseract.image_to_string(str_img)

str_img2 = Image.open('ocr_test/string2.png')
str2 = pytesseract.image_to_string(str_img2)

print(str)

print(str2)
