import csv
import os
import subprocess
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def generate_image(item_name, magick_path, tiff_directory, jpg_directory):
    # Construct the full paths for the TIFF and JPG files
    tiff_path = os.path.join(tiff_directory, f'{item_name}.tif')
    jpg_path = os.path.join(jpg_directory, f'{item_name}.jpg')

    # Print the paths for debugging purposes
    print(f'TIFF Path: {tiff_path}')
    print(f'JPG Path: {jpg_path}')

    # Create the command to convert the TIFF to JPG using ImageMagick
    command = [magick_path, tiff_path, '-background', 'white', '-flatten', jpg_path]

    # Print command for debugging
    print(f'Executing command: {" ".join(command)}')

    # Execute the command
    result = subprocess.run(command, capture_output=True, text=True)

    # Print the result and any errors for debugging
    print(f'Command output: {result.stdout}')
    print(f'Command error: {result.stderr}')


def main():
    # Load environment variables
    magick_path = os.getenv('MAGICK_PATH')
    tiff_directory = os.getenv('TIFF_DIRECTORY')
    jpg_directory = os.getenv('JPEG_DIRECTORY')

    # Debugging prints
    print(f'MAGICK_PATH: {magick_path}')
    print(f'TIFF_DIRECTORY: {tiff_directory}')
    print(f'JPEG_DIRECTORY: {jpg_directory}')

    # CSV file containing the list of image names
    csv_file = 'data.csv'

    # Open the CSV file and read its contents
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader, None)  # Skip the header row if it exists
        if header is None:
            print("CSV file is empty or does not have a header.")
            return

        for row in reader:
            if not row:
                print("Skipping empty row.")
                continue

            if len(row) < 1:
                print("Row does not contain enough columns.")
                continue

            item_name = row[0]  # Assuming the first column contains the image names

            # Generate the image
            generate_image(item_name, magick_path, tiff_directory, jpg_directory)


if __name__ == "__main__":
    main()
