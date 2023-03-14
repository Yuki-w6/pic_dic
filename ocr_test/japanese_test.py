import pytesseract
from PIL import Image

str_img = Image.open('ocr_test/japanese_test1.png')
str = pytesseract.image_to_string(str_img, lang="jpn")

print(str)
