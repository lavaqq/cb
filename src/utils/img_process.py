import os
import cv2
import numpy as np
from PIL import Image

current_dir = os.getcwd()


def convert(dir_path):
    for f in os.listdir(os.path.join(dir_path, 'processed')):
        if not f.lower().endswith('.png'):
            f_path = os.path.join(dir_path, 'processed', f)
            f_dir = os.path.join(dir_path, 'processed')
            with Image.open(f_path) as img:
                new_f = os.path.splitext(f)[0] + '.png'
                img.save(os.path.join(f_dir, new_f))
                os.remove(f_path)
