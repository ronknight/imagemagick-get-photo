import csv
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def generate_image(item_name, magick_path, tiff_directory, jpg_directory):
    tiff_path = os.path.join(tiff_directory, f'{item_name}.tif')
    jpg_path = os.path.join(jpg_directory, f'{item_name}.jpg')

    command = f'"{magick_path}" "{tiff_path}" -background white -alpha remove "{jpg_path}"'
    os.system(command)

def main():
    csv_file = 'data.csv'
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            item_name = row[0]
            magick_path = os.getenv('MAGICK_PATH')
            tiff_directory = os.getenv('TIFF_DIRECTORY')
            jpg_directory = os.getenv('JPEG_DIRECTORY')
            generate_image(item_name, magick_path, tiff_directory, jpg_directory)

if __name__ == "__main__":
    main()
