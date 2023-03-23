import os
import shutil
from PIL import Image


def c_r(dir_path, dst_path):
    dst_dir = os.path.join(dst_path, 'processed')
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
    os.mkdir(dst_dir)
    i = 0
    for f in os.listdir(dir_path):
        f_path = os.path.join(dir_path, f)
        if os.path.isfile(f_path) and any(f_path.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png']):
            ext = os.path.splitext(f_path)[1]
            new_filename = str(i) + ext
            src_path = os.path.join(dir_path, f)
            dst_path = os.path.join(dst_dir, new_filename)
            shutil.copyfile(src_path, dst_path)
            i += 1
    convert(dst_dir)


def convert(dir_path):
    for f in os.listdir(dir_path):
        if not f.lower().endswith('.png'):
            f_path = os.path.join(dir_path, f)
            f_dir = dir_path
            with Image.open(f_path) as img:
                new_f = os.path.splitext(f)[0] + '.png'
                img.save(os.path.join(f_dir, new_f))
                os.remove(f_path)
