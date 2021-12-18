try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

import cv2
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# OCR - Optyczne rozpoznawanie znaków (Optical character recognition)

# Czytanie zdjęcia
img = cv2.imread('city.jpg')

# Reprezentacja zdjęcia w liczbach
print(type(img))
print(img.shape)

# Wyświetlanie zdjęcia
cv2.imshow('image-city', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Konwertowanie zdjęcia do czerni i bieli
img_convert = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Czy cv2 przetrzymuje obraz w postaci RGB?
plt.imshow(img)
plt.show()
