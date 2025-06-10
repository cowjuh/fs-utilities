# PNG to Excel Converter

A Python script that converts PNG images in a specified folder into an organized Excel spreadsheet with thumbnails and detailed image metadata.

## Features

- Converts all PNG images in a specified folder to an Excel spreadsheet
- Creates thumbnails of each image
- Includes detailed metadata for each image:
  - Image thumbnail
  - Filename
  - Width (in pixels)
  - Height (in pixels)
  - Width (in inches)
  - Height (in inches)
  - Color mode
  - Image format

## Requirements

- Python 3.9 or higher
- Required Python packages (automatically installed if missing):
  - Pillow
  - openpyxl

## Installation

1. Ensure you have Python 3.9+ installed on your system
2. Clone or download this repository
3. Navigate to the script directory

## Usage

Run the script from the terminal, providing the path to your PNG folder:

```bash
python3 png_to_excel_user_friendly.py /path/to/your/png/folder
```

For example, if your PNG files are in a folder called "images" in your current directory:
```bash
python3 png_to_excel_user_friendly.py ./images
```

The script will:
1. Process all PNG files in the specified folder
2. Create a new folder named "[Your Folder Name] EXCEL" next to your images
3. Generate thumbnails for all PNG files
4. Create an Excel file named `png_info.xlsx` with all the image information

## Output

The script creates an Excel file with the following columns:
- Image: Thumbnail preview of the PNG
- Filename: Original filename
- Width (px): Image width in pixels
- Height (px): Image height in pixels
- Width (in): Image width in inches (calculated at 300 DPI)
- Height (in): Image height in inches (calculated at 300 DPI)
- Mode: Color mode (e.g., RGB, RGBA)
- Format: Image format (PNG)

## Notes

- The script automatically handles missing dependencies
- If no PNG files are found in the specified folder, the script will notify you and exit
- Thumbnails are created at 128x128 pixels maximum while maintaining aspect ratio
- The Excel file is saved in a new folder to keep your original files organized 