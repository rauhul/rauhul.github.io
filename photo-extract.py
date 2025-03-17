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
from datetime import datetime

def find_files(directory):
    _directory = os.path.basename(directory)
    image_data = []
    
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
                    
                    # Get date and time from EXIF for sorting
                    date_time = exif.get('DateTime', exif.get('DateTimeOriginal', exif.get('DateTimeDigitized', None)))
                    
                    # Create a structure to store all image data
                    data = {
                        'file': file,
                        'focal_length': focal_length,
                        'aperture': aperture,
                        'shutter_speed': shutter_speed,
                        'iso': iso,
                        'wide': wide,
                        'date_time': date_time
                    }
                    
                    image_data.append(data)
                else:
                    print(f"File: {file_path} has no EXIF data.")
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")
    
    # Sort images by date taken
    def get_date_key(item):
        if item['date_time']:
            try:
                return datetime.strptime(item['date_time'], '%Y:%m:%d %H:%M:%S')
            except (ValueError, TypeError):
                return datetime.min
        return datetime.min
    
    image_data.sort(key=get_date_key)
    
    # Print the sorted image data
    print(f"  photos:")
    for data in image_data:
        focal_length_str = int(data['focal_length'])
        print(
f"""  - url: https://rauhulpic.dws.rip/download/pics/{_directory}/{data['file']}
    focal-length: {focal_length_str}
    aperture: {data['aperture']}
    shutter-speed: {data['shutter_speed']}
    iso: {data['iso']}
    wide: {str(data['wide']).lower()}""")

def main():
    parser = argparse.ArgumentParser(description='Find and print all file paths in a directory.')
    parser.add_argument('-d', '--directory', type=str, required=True,
                        help='Directory to search for files')
    args = parser.parse_args()
    find_files(args.directory)

if __name__ == "__main__":
    main()
