from utils import f_prc
from utils import img_prc
import sys
import argparse
import os


def main():
    parser = argparse.ArgumentParser(description='Process some images.')
    parser.add_argument('src_path', type=str, help='the directory containing the images to process')
    parser.add_argument('dst_path', type=str, help='the destination directory for the processed images')
    parser.add_argument('-b', '--blur', action='store_true', help='apply a blur effect to the images')
    parser.add_argument('-c', '--crop', action='store_true', help='crop the images to a square shape')
    args = parser.parse_args()
    src_p = args.src_path
    dst_p = args.dst_path
    blur = args.blur
    crop = args.crop
    if not os.path.isdir(src_p):
        print(f"Error: '{src_p}' is not a directory.")
        sys.exit(1)
    if not blur and not crop:
        print("Error: You must specify at least one operation to perform on the images.")
        sys.exit(1)
    f_prc.rc(src_p, dst_p)
    if blur and crop:
        img_prc.crop(dst_p)
        img_prc.blur(dst_p)
        sys.exit(1)
    if blur:
        img_prc.crop(dst_p)
        sys.exit(1)
    if crop:
        img_prc.blur(dst_p)
        sys.exit(1)
if __name__ == '__main__':
    main()
