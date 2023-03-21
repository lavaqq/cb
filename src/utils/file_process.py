import os

def rename(directory_path):
    count = 0
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path) and any(file_path.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png']):
            new_filename = str(count) + '.png'
            os.rename(file_path, os.path.join(directory_path, new_filename))
            count += 1
        else:
            continue
