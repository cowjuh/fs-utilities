# Media to Scale Sheet Converter

This script converts images in a specified folder into a scale sheet showing the images at their actual print size (300 DPI) with metadata. It's particularly useful for designers and printers who need to verify the physical dimensions of their images.

## Features

- Supports multiple image formats (PNG, JPG, JPEG, TIF, TIFF)
- Shows images at their actual print size (300 DPI)
- Displays detailed metadata for each image:
  - Original dimensions in pixels
  - Physical dimensions in inches
  - Color mode
  - File format
- Multiple output formats:
  - PDF (default, actual print size)
  - PNG (2x scale for better visibility)
  - JPG (2x scale for better visibility)
- Customizable output filename and location

## Requirements

- Python 3.9 or higher
- Pillow (PIL) library

## Installation

1. Make sure you have Python 3.9+ installed
2. Install the required package:
   ```bash
   pip install Pillow
   ```

## Usage

```bash
python3 media_to_scale_sheet.py -i /path/to/input/folder -o /path/to/output/folder [-n output_name] [-f format]
```

### Arguments

- `-i, --input`: Path to the folder containing media files (required)
- `-o, --output`: Path to the output folder (required)
- `-n, --name`: Name for the output file (default: scale_sheet)
- `-f, --format`: Output format: pdf, png, or jpg (default: pdf)

### Examples

1. Create a PDF scale sheet (default):
   ```bash
   python3 media_to_scale_sheet.py -i ./my_images -o ./output -n my_scale_sheet
   ```

2. Create a PNG scale sheet with larger images:
   ```bash
   python3 media_to_scale_sheet.py -i ./my_images -o ./output -n my_scale_sheet -f png
   ```

3. Create a JPG scale sheet with larger images:
   ```bash
   python3 media_to_scale_sheet.py -i ./my_images -o ./output -n my_scale_sheet -f jpg
   ```

## Output Formats

- **PDF**: Shows images at their actual print size (300 DPI)
- **PNG/JPG**: Shows images at 2x scale for better visibility while maintaining aspect ratios
  - Higher quality output (95% quality for JPG)
  - Larger file sizes but better for screen viewing

## Customization

The script can be customized by modifying several parameters:

1. DPI for inch calculations:
   - Find the line with `w_in = w / 300`
   - Change 300 to your desired DPI

2. Layout settings:
   - Adjust padding, label height, and font sizes in the "Layout settings" section

3. Output scaling:
   - Modify the `scale` values in the `OUTPUT_FORMATS` dictionary
   - Current settings: PDF=1x, PNG/JPG=2x

## Troubleshooting

- If you get a font error, the script will fall back to the default font
- Make sure your input folder contains supported image files
- Check that you have write permissions in the output directory
- For large images, consider using PDF format to maintain actual print size

## License

This script is provided under the MIT License. Feel free to modify and distribute it as needed. 