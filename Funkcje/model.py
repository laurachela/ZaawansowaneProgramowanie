import cv2

# Gotowy model klasyfikacji zdjęć - algorytm MibileNet, zbiór danych coco
config_file = 'Modele/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model = 'frozen_inference_graph.pb'
model = cv2.dnn_DetectionModel(frozen_model, config_file)

# Konfiguracja gotowego modelu
model.setInputSize(320, 320)
model.setInputScale(1.0 / 127.5)
model.setInputMean((127.5, 127.5, 127.5))
model.setInputSwapRB(True)

accuracyThreshold = 0.52
