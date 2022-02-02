import cv2
import numpy as np
import glob
import Funkcje.model as funct_mod
from Funkcje.functions import count_person
from Funkcje.functions import img_boxes_draw

path = glob.glob("Fotos/*.jpg")
i = 0
for jpgPhoto in path:
    image = cv2.imread(jpgPhoto)
    classIndex, confidence, bbox = funct_mod.model.detect(image, funct_mod.accuracyThreshold)
    print("\nIndexy z labels widocznych na zdjeciach obiektow:\n", classIndex)
    img_boxes_draw(classIndex, confidence, bbox, image)
    imgRotate = np.hstack((image,))
    cv2.imshow(count_person(classIndex, i), imgRotate)
    i += 1
    cv2.waitKey()
