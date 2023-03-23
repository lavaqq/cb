## Installation

To use this script, you need to have Python 3 installed on your machine.

You can install the required packages by running the following command:

```bash
pip install -r requirements.txt
```

## Usage

To use the tool, run the following command:

```bash
python image_processing.py SRC_PATH DST_PATH [-b] [-c]
```

- `SRC_PATH` is the path to the directory containing the images to process.
- `DST_PATH` is the path to the directory where the processed images will be saved.
- `-b` or `--blur` applies a blur effect to the images.
- `-c` or `--crop` crops the black border of the images.

## Example

```bash
python image_processing.py ./input_images ./output_images -b -c
```

This command will process the images in the `./input_images` directory, apply a blur effect, crop black border, and save the processed images in the `./output_images` directory.
