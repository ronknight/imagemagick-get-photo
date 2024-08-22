
<p><a target="_blank" href="https://app.eraser.io/workspace/I2gu6P6fOaPpL3pY480G" id="edit-in-eraser-github-link"><img alt="Edit in Eraser" src="https://firebasestorage.googleapis.com/v0/b/second-petal-295822.appspot.com/o/images%2Fgithub%2FOpen%20in%20Eraser.svg?alt=media&amp;token=968381c8-a7e7-472a-8ed6-4a6626da5501"></a></p>

# [﻿Photo Generator](https://github.com/ronknight/imagemagick-get-photo) 
#### This Python script generates JPG images from TIFF files using ImageMagick. It reads item names from a CSV file, locates the corresponding TIFF files in a specified directory, and generates JPG images in another directory.

<p align="center">
<a href="https://twitter.com/PinoyITSolution"><img src="https://img.shields.io/twitter/follow/PinoyITSolution?style=social"></a>
<a href="https://github.com/ronknight?tab=followers"><img src="https://img.shields.io/github/followers/ronknight?style=social"></a>
<a href="https://github.com/ronknight/ronknight/stargazers"><img src="https://img.shields.io/github/stars/BEPb/BEPb.svg?logo=github"></a>
<a href="https://github.com/ronknight/ronknight/network/members"><img src="https://img.shields.io/github/forks/BEPb/BEPb.svg?color=blue&logo=github"></a>
  <a href="https://youtube.com/@PinoyITSolution"><img src="https://img.shields.io/youtube/channel/subscribers/UCeoETAlg3skyMcQPqr97omg"></a>
<a href="https://github.com/ronknight/imagemagick-get-photo/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
<a href="https://github.com/ronknight/imagemagick-get-photo/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
<a href="#"><img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg"></a>
<a href="https://github.com/ronknight"><img src="https://img.shields.io/badge/Made%20with%20%F0%9F%A4%8D%20by%20-%20Ronknight%20-%20red"></a>
</p>

<p align="center">
  <a href="#prerequisites">Prerequisites</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#notes">Notes</a> •
  <a href="#diagrams">Diagrams</a> •
</p>

```bash
MAGICK_PATH="C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"
TIFF_DIRECTORY="\\\\172.16.5.6\\ImageRepository\\Master-Tiff"
JPEG_DIRECTORY="C:\\Users\\rona\\OneDrive - 4sgm.com\\Email Catalog"
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
