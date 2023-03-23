import os
import cv2
import numpy as np


def crop(dst_path):
    i = 0
    for f in os.listdir(dst_path):
        f_path = os.path.join(dst_path, f)
        img = cv2.imread(f_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        contours, hierarchy = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        x, y, w, h = cv2.boundingRect(contours[0])
        if x == 0 and y == 0 and w == gray.shape[1] and h == gray.shape[0]:
            continue
        cropped_img = img[y:y+h, x:x+w]
        cv2.imwrite(f_path, cropped_img)
        i += 1
    print(f"Info: {i} images cropped.")



def blur(dst_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
    for f in os.listdir(dst_path):
        f_path = os.path.join(dst_path, f)
        img = cv2.imread(f_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        mask_img = np.zeros(img.shape, dtype='uint8')
        for (x, y, w, h) in faces:
            center = (x + w//2, y + h//2)
            radius = w//2
            cv2.circle(mask_img, center, radius, (255, 255, 255), -1)
        img_all_blurred = cv2.GaussianBlur(img, (99, 99), 0)
        img = np.where(mask_img > 0, img_all_blurred, img)
        cv2.imwrite(f_path, img)
    print(f"Info: images blurred.")
