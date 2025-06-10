# software-studios

This repository contains a collection of user-friendly scripts and tools for various software and media processing tasks.

## Available Scripts

### Media to Excel Converter (`scripts/png_to_excel_user_friendly`)

A Python script that converts various media files (PNG, TIFF, JPEG, PDF) in a specified folder into an organized Excel spreadsheet. The spreadsheet includes thumbnails and detailed metadata for each file (filename, dimensions in pixels and inches, color mode, and format).

#### Features:
- Supports multiple file formats (PNG, TIFF, JPEG, PDF)
- Creates high-quality thumbnails (256x256 pixels)
- Organizes thumbnails in a separate subfolder
- Includes detailed metadata in the Excel output
- Customizable output filename

#### Usage:
```bash
python3 media_to_excel.py -i /path/to/input/folder -o /path/to/output/folder [-n output_name]
```

#### Options:
- `-i, --input`: Path to the folder containing media files (required)
- `-o, --output`: Path to the output folder (required)
- `-n, --name`: Name for the output Excel file (optional, defaults to "media_info")

#### Example:
```bash
python3 media_to_excel.py -i "/path/to/images" -o "/path/to/output" -n "my_media_info"
```

This will:
1. Process all supported files in the input folder
2. Create thumbnails in a "thumbnails" subfolder
3. Generate an Excel file with metadata and image previews

---

More scripts and tools will be added to this repository over time.
