# Media to Excel Converter

A Python script that converts various media files (PNG, TIFF, JPEG, PDF) in a specified folder into an organized Excel spreadsheet with thumbnails and detailed metadata.

## Features

- Supports multiple file formats (PNG, TIFF, JPEG, PDF)
- Creates high-quality thumbnails (256x256 pixels)
- Organizes thumbnails in a separate subfolder
- Includes detailed metadata for each file:
  - Image thumbnail
  - Filename
  - Width (in pixels)
  - Height (in pixels)
  - Width (in inches)
  - Height (in inches)
  - Color mode
  - Image format

## macOS Setup

1. Install Homebrew (macOS package manager) if you don't have it:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. Install Python using Homebrew:
   ```bash
   brew install python@3.9
   ```

3. Verify Python installation:
   ```bash
   python3 --version
   ```
   You should see Python 3.9.x or higher

4. Install pip (Python package manager) if it's not already installed:
   ```bash
   curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
   python3 get-pip.py
   ```

## Requirements

- Python 3.9 or higher
- Required Python packages (automatically installed if missing):
  - Pillow
  - openpyxl
  - pdf2image (for PDF support)

## Installation

1. Ensure you have Python 3.9+ installed on your system
2. Clone or download this repository
3. Navigate to the script directory

## Usage

Run the script from the terminal, providing the input and output paths:

```bash
python3 media_to_excel.py -i /path/to/input/folder -o /path/to/output/folder [-n output_name]
```

For example:
```bash
python3 media_to_excel.py -i "./images" -o "./output" -n "my_media_info"
```

The script will:
1. Process all supported files in the input folder
2. Create a "thumbnails" subfolder in the output directory
3. Generate thumbnails for all media files
4. Create an Excel file with all the file information

## Output

The script creates an Excel file with the following columns:
- Image: Thumbnail preview (256x256 pixels)
- Filename: Original filename
- Width (px): Image width in pixels
- Height (px): Image height in pixels
- Width (in): Image width in inches (calculated at 300 DPI)
- Height (in): Image height in inches (calculated at 300 DPI)
- Mode: Color mode (e.g., RGB, RGBA)
- Format: Original file format

## Notes

- The script automatically handles missing dependencies
- If no supported files are found in the specified folder, the script will notify you and exit
- Thumbnails are created at 256x256 pixels maximum while maintaining aspect ratio
- The Excel file and thumbnails are saved in the specified output directory 