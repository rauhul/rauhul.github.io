#! /usr/bin/env -S uv run --script

# /// script
# dependencies = [
#   "pillow",
# ]
# ///

import os
import argparse
from PIL import Image
from PIL.ExifTags import TAGS

def find_files(directory):
    _directory = os.path.basename(directory)
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.startswith('.'):
                continue
            file_path = os.path.join(root, file)
            try:
                image = Image.open(file_path)
                exif_data = image._getexif()
                if exif_data:
                    exif = {TAGS.get(tag): value for tag, value in exif_data.items()}
                    focal_length = exif.get('FocalLength', 'N/A')
                    aperture = exif.get('FNumber', 'N/A')
                    exposure_time = exif.get('ExposureTime', 'N/A')
                    shutter_speed = 1 / exposure_time
                    iso = exif.get('ISOSpeedRatings', 'N/A')
                    width, height = image.size
                    wide = width > height
                    print(
f"""
  - url: https://rauhulpic.dws.rip/download/pics/{_directory}/{file}
    focal-length: {int(focal_length)}
    aperture: {aperture}
    shutter-speed: {shutter_speed}
    iso: {iso}
    wide: {str(wide).lower()}
""".strip('\n'))
                else:
                    print(f"File: {file_path} has no EXIF data.")
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description='Find and print all file paths in a directory.')
    parser.add_argument('-d', '--directory', type=str, required=True,
                        help='Directory to search for files')
    args = parser.parse_args()
    find_files(args.directory)

if __name__ == "__main__":
    main()
    
