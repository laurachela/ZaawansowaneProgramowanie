try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

import cv2
# import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# OCR - Optyczne rozpoznawanie znaków (Optical character recognition)


def ocr_core(img1):
    text = pytesseract.image_to_string(img1)
    return text


# Czytanie zdjęcia
img = cv2.imread('text5.jpg')

# Reprezentacja zdjęcia w liczbach
# print(type(img))
# print(img.shape)

# Wyświetlanie zdjęcia
cv2.imshow('image-text1', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Konwertowanie zdjęcia do czerni i bieli
# img_convert = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# get grayscale image


def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# get noise removal


def remove_noise(image):
    return cv2.medianBlur(image, 5)

# theresholding


def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Czy cv2 przetrzymuje obraz w postaci RGB?
# plt.imshow(img)
# plt.show()


img = get_grayscale(img)
img = thresholding(img)
img = remove_noise(img)

print(ocr_core(img))
