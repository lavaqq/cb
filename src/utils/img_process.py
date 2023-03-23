import os
import cv2
import numpy as np
from PIL import Image


def convert(dir_path):
    for f in os.listdir(os.path.join(dir_path, 'processed')):
        if not f.lower().endswith('.png'):
            f_path = os.path.join(dir_path, 'processed', f)
            f_dir = os.path.join(dir_path, 'processed')
            with Image.open(f_path) as img:
                new_f = os.path.splitext(f)[0] + '.png'
                img.save(os.path.join(f_dir, new_f))
                os.remove(f_path)


def crop(dir_path):
    for f in os.listdir(os.path.join(dir_path, 'processed')):
        f_path = os.path.join(dir_path, 'processed', f)
        img = cv2.imread(f_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        contours, hierarchy = cv2.findContours(
            gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        x, y, w, h = cv2.boundingRect(contours[0])
        cropped_img = img[y:y+h, x:x+w]
        cv2.imwrite(f_path, cropped_img)


def blur(dir_path):
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
    for f in os.listdir(os.path.join(dir_path, 'processed')):
        f_path = os.path.join(dir_path, 'processed', f)
        img = cv2.imread(f_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5)
        mask_img = np.zeros(img.shape, dtype='uint8')
        for (x, y, w, h) in faces:
            center = (x + w//2, y + h//2)
            radius = w//2
            cv2.circle(mask_img, center, radius, (255, 255, 255), -1)
        img_all_blurred = cv2.GaussianBlur(img, (85, 85), 0)
        img = np.where(mask_img > 0, img_all_blurred, img)
        cv2.imwrite(f_path, img)
