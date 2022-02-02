import cv2
import numpy as np
import collections


def count_person(class_array, photo_number: int) -> str:
    person_image = np.array(class_array)
    count_person_image = collections.Counter(person_image)[1]
    print("Na zdjęciu nr ", photo_number + 1, " znajduje się: ", count_person_image, " osób ")
    text = f'Zdjęcie nr  {photo_number + 1}'
    return text


def img_boxes_draw(class_index_draw, confidence_draw, bboxdraw, img_draw):
    for x, conf, boxes in zip(class_index_draw.flatten(), confidence_draw.flatten(), bboxdraw):
        if x == 1:
            cv2.rectangle(img_draw, boxes, (80, 220, 100), 2)
            file_name = 'Modele/labels.txt'
            with open(file_name, 'rt') as fpt:
                class_labels = fpt.read().rsplit('\n')
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.5
            cv2.putText(img_draw, class_labels[x - 1], (boxes[0] - 8, boxes[1] - 8),
                        font, fontScale=font_scale,
                        color=(0, 255, 0), thickness=1)
