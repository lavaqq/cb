import os
import shutil
from PIL import Image


def ren_cp_conv(dir_path, dst_path):
    if not os.path.isdir(dst_path):
        print(f"Error: '{dst_path}' is not a directory.")
        sys.exit(1)
    if os.path.exists(dst_path):
        shutil.rmtree(dst_path)
    os.mkdir(dst_path)
    i = 0
    for f in os.listdir(dir_path):
        f_path = os.path.join(dir_path, f)
        if os.path.isfile(f_path) and any(f_path.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', 'webp']):
            ext = os.path.splitext(f_path)[1]
            new_filename = str(i) + ext
            src_path = os.path.join(dir_path, f)
            dst_path = os.path.join(dst_path, new_filename)
            shutil.copyfile(src_path, dst_path)
            i += 1
    convert(dst_path)


def convert(dir_path):
    for f in os.listdir(dir_path):
        if not f.lower().endswith('.png'):
            f_path = os.path.join(dir_path, f)
            f_dir = dir_path
            with Image.open(f_path) as img:
                new_f = os.path.splitext(f)[0] + '.png'
                img.save(os.path.join(f_dir, new_f))
                os.remove(f_path)
