import os
import shutil

def copy(dir_path):
    dst_dir = os.path.join(dir_path, 'processed')
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
    os.mkdir(dst_dir)
    for f in os.listdir(dir_path):
        f_path = os.path.join(dir_path, f)
        if os.path.isfile(f_path) and any(f_path.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png']):
            src_path = os.path.join(dir_path, f)
            dst_path = os.path.join(dst_dir, f)
            shutil.copyfile(src_path, dst_path)


def rename(dir_path):
    i = 0
    for f in os.listdir(os.path.join(dir_path, 'processed')):
        ext = os.path.splitext(f)[1]
        new_filename = str(i) + ext
        src = os.path.join(dir_path, 'processed', f)
        dst = os.path.join(dir_path, 'processed', new_filename)
        os.rename(src, dst)
        i += 1