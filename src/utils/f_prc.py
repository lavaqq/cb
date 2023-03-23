import os
import shutil
import sys
import getch
from PIL import Image


def rc(src_p, dst_p):
    if os.path.exists(dst_p):
        print(f"Error: '{dst_p}' already exist, do you want to continue? (y/n): ")
        key = getch.getch()
        if key == "y":
            shutil.rmtree(dst_p)
        else:
            sys.exit(1)
    os.mkdir(dst_p)
    i = 0
    for f in os.listdir(src_p):
        f_path = os.path.join(src_p, f)
        if os.path.isfile(f_path) and any(f_path.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', 'webp']):
            ext = os.path.splitext(f_path)[1]
            new_f = str(i) + ext
            src_f = f_path
            dst_f = os.path.join(dst_p, new_f)
            shutil.copyfile(src_f, dst_f)
            i += 1
    print(f"Info: {i} images transferred to '{dst_p}'.")