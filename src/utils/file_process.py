import os
import shutil

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
