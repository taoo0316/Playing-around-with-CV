# https://towardsdatascience.com/build-optical-character-recognition-ocr-in-python-28d1c7b77da3

from PIL import Image
import pytesseract
import numpy as np
import cv2


filename = '/Users/zwt2000/Desktop/cute/download.jpeg'
img = np.array(Image.open(filename))
text = pytesseract.image_to_string(img)

norm_img = np.zeros((img.shape[0], img.shape[1]))
img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
img = cv2.GaussianBlur(img, (1, 1), 0)

print(text)