# PNG to Excel Converter

A user-friendly Python script that converts PNG images in a selected folder into an organized Excel spreadsheet with thumbnails and detailed image metadata.

## Features

- Converts all PNG images in a selected folder to an Excel spreadsheet
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
  - tkinter (usually comes with Python)

## Installation

1. Ensure you have Python 3.9+ installed on your system
2. Clone or download this repository
3. Navigate to the script directory

## Usage

1. Open Terminal and navigate to the script directory:
   ```bash
   cd /path/to/scripts/png_to_excel_user_friendly
   ```
2. Run the script:
   ```bash
   python3 png_to_excel_user_friendly.py
   ```
3. A folder selection dialog will appear - select the folder containing your PNG images
4. The script will:
   - Create a new folder named "[Your Folder Name] EXCEL" next to your images
   - Generate thumbnails for all PNG files
   - Create an Excel file named `png_info.xlsx` with all the image information
5. When complete, a message will show the location of the saved Excel file

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
- If no PNG files are found in the selected folder, the script will notify you and exit
- Thumbnails are created at 128x128 pixels maximum while maintaining aspect ratio
- The Excel file is saved in a new folder to keep your original files organized 