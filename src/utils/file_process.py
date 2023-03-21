import os
import shutil

def copy(dir_path):
    dst_dir = os.path.join(dir_path, "processed")
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
    os.mkdir(dst_dir)
    for f in os.listdir(dir_path):
        f_path = os.path.join(dir_path, f)
        if os.path.isfile(f_path) and any(f_path.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png']):
            src_path = os.path.join(dir_path, f)
            dst_path = os.path.join(dst_dir, f)
            shutil.copyfile(src_path, dst_path)



def rename(directory_path):
    count = 0
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path) and any(file_path.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png']):
            new_filename = str(count) + ext
            os.rename(file_path, os.path.join(directory_path, new_filename))
            count += 1
        else:
            continue
