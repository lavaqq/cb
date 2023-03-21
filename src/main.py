from utils import file_process as fp
from utils import img_process as ip

import sys
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description='Process some images.')
    parser.add_argument('image_dir', type=str, help='the directory containing the images to process')
    parser.add_argument('-r', '--rename', action='store_true', help='rename the images')
    parser.add_argument('-b', '--blur', action='store_true', help='apply a blur effect to the images')
    parser.add_argument('-c','--crop', action='store_true', help='crop the images to a square shape')
    args = parser.parse_args()

    image_dir = args.image_dir
    rename = args.rename
    blur = args.blur
    crop = args.crop

    if not os.path.isdir(image_dir):
        print(f"Error: '{image_dir}' is not a directory.")
        sys.exit(1)


if __name__ == '__main__':
    main()