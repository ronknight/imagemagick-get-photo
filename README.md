<p><a target="_blank" href="https://app.eraser.io/workspace/I2gu6P6fOaPpL3pY480G" id="edit-in-eraser-github-link"><img alt="Edit in Eraser" src="https://firebasestorage.googleapis.com/v0/b/second-petal-295822.appspot.com/o/images%2Fgithub%2FOpen%20in%20Eraser.svg?alt=media&amp;token=968381c8-a7e7-472a-8ed6-4a6626da5501"></a></p>

# [﻿Photo Generator](https://github.com/ronknight/imagemagick-get-photo) 
#### This Python script generates JPG images from TIFF files using ImageMagick. It reads item names from a CSV file, locates the corresponding TIFF files in a specified directory, and generates JPG images in another directory.
 [﻿Prerequisites](#prerequisites) • [﻿Installation](#installation) • [﻿Usage](#usage) • [﻿Notes](#notes) • [﻿Diagrams](#diagrams) • 

---

## Prerequisites
- Python 3.x
- ImageMagick installed and accessible from the command line
- A CSV file with item names in the first column
- A directory containing TIFF files with names matching the item names in the CSV file
## Installation
1. Clone the repository or download the source code.
2. Install the required Python package by running `pip install python-dotenv` .
3. Create a `.env`  file in the project directory and add the following environment variables:
```bash
MAGICK_PATH=/path/to/magick
TIFF_DIRECTORY=/path/to/tiff/files
JPEG_DIRECTORY=/path/to/output/jpg/files
```
Replace the paths with the actual paths on your system.

## Usage
1. Open a terminal or command prompt and navigate to the project directory.
2. Run the script with `python getphoto.py` .
The script will read the item names from the `data.csv` file, locate the corresponding TIFF files in the specified `TIFF_DIRECTORY`, and generate JPG images in the `JPEG_DIRECTORY`.

## Notes
- The script assumes that the CSV file is named `data.csv`  and is located in the project directory.
- The TIFF and JPG file names will be the same as the item names in the CSV file, with the appropriate file extensions.
- If a TIFF file is not found for an item name, the script will skip that item and continue with the next one.



<!-- eraser-additional-content -->
## Diagrams
<!-- eraser-additional-files -->
<a href="/README-Photo Generator Flowchart-1.eraserdiagram" data-element-id="RpYABPjUKBhzHrss4qLWb"><img src="/.eraser/I2gu6P6fOaPpL3pY480G___3Jivg2tjMecMlrHwbIVIBR8f7U03___---diagram----b0acd42499f7fb861d7a612f9d903ba8-Photo-Generator-Flowchart.png" alt="" data-element-id="RpYABPjUKBhzHrss4qLWb" /></a>
<!-- end-eraser-additional-files -->
<!-- end-eraser-additional-content -->
<!--- Eraser file: https://app.eraser.io/workspace/I2gu6P6fOaPpL3pY480G --->