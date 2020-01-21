import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

def load_image(file_path):
    return cv2.imread(file_path)

def extract_label(file_name):
    return 1 if "dog" in file_name else 0

def preprocess_image(img, side=96):
    min_side = min(img.shape[0], img.shape[1])
    img = img[:min_side, :min_side]
    img = cv2.resize(img, (side,side))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img / 255.0

def get_prediction(prediction):
    if prediction[0] > prediction[1]:
        return "cat"
    else:
        return "dog"


eval_model = tf.keras.models.load_model("final_model.h5")
test_path = "C:/Users/Daniel/.keras/datasets/cats_and_dogs_test/"
image_files = os.listdir(test_path)
eval_images = [preprocess_image(load_image(test_path + file)) for file in image_files]
eval_predictions = eval_model.predict(np.expand_dims(eval_images, axis=-1))
for i in range(len(eval_predictions)):
  print(image_files[i], get_prediction(eval_predictions[i]))
