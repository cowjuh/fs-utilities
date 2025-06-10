#!/usr/bin/env python3
"""
Media to Excel Converter
=======================

This script converts all PNG images in a specified folder into an Excel file with thumbnails and metadata.

Usage:
    python3 media_to_excel.py -i /path/to/input/folder -o /path/to/output/folder

The script will:
1. Process all PNG files in the input folder
2. Create thumbnails and collect metadata
3. Save an Excel file with the information in the output folder

Requirements:
- Python 3.9+
- Pillow
- openpyxl
"""
import os
import sys
import subprocess
import importlib.util
import argparse

# List of required packages
REQUIRED_PACKAGES = ["Pillow", "openpyxl"]

# Check and install missing packages
for pkg in REQUIRED_PACKAGES:
    if importlib.util.find_spec(pkg) is None:
        print(f"Installing missing package: {pkg}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

try:
    from PIL import Image
    from openpyxl import Workbook
    from openpyxl.drawing.image import Image as XLImage
    from openpyxl.utils import get_column_letter
except ImportError as e:
    print(f"Failed to import required modules: {e}")
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Convert PNG files in a folder to an Excel spreadsheet with metadata.')
    parser.add_argument('-i', '--input', required=True, help='Path to the folder containing PNG files')
    parser.add_argument('-o', '--output', required=True, help='Path to the output folder for Excel file and thumbnails')
    args = parser.parse_args()

    SRC_DIR = args.input
    DEST_DIR = args.output

    if not os.path.isdir(SRC_DIR):
        print(f"Error: Input directory '{SRC_DIR}' is not a valid directory")
        sys.exit(1)

    os.makedirs(DEST_DIR, exist_ok=True)

    png_files = [f for f in os.listdir(SRC_DIR) if f.lower().endswith('.png')]
    if not png_files:
        print(f"No PNG files found in '{SRC_DIR}'")
        sys.exit(0)

    print(f"Processing {len(png_files)} PNG files...")

    wb = Workbook()
    ws = wb.active
    ws.title = "PNG Info"
    headers = ["Image", "Filename", "Width (px)", "Height (px)", "Width (in)", "Height (in)", "Mode", "Format"]
    ws.append(headers)
    ws.column_dimensions[get_column_letter(1)].width = 20
    for i in range(2, len(headers)+1):
        ws.column_dimensions[get_column_letter(i)].width = 20

    row = 2
    for fname in png_files:
        path = os.path.join(SRC_DIR, fname)
        try:
            img = Image.open(path)
        except Exception as e:
            print(f"Skipping {fname}: {e}")
            continue
        w, h = img.size
        w_in = w / 300
        h_in = h / 300
        mode = img.mode
        fmt = img.format or 'PNG'
        thumb = img.copy()
        thumb.thumbnail((128, 128), Image.LANCZOS)
        thumb_path = os.path.join(DEST_DIR, f"thumb_{fname}")
        thumb.save(thumb_path)
        xl_img = XLImage(thumb_path)
        ws.row_dimensions[row].height = 100
        ws.add_image(xl_img, f"A{row}")
        ws.cell(row=row, column=2, value=fname)
        ws.cell(row=row, column=3, value=w)
        ws.cell(row=row, column=4, value=h)
        ws.cell(row=row, column=5, value=round(w_in, 2))
        ws.cell(row=row, column=6, value=round(h_in, 2))
        ws.cell(row=row, column=7, value=mode)
        ws.cell(row=row, column=8, value=fmt)
        row += 1

    out_path = os.path.join(DEST_DIR, 'png_info.xlsx')
    wb.save(out_path)
    print(f"\nDone! Excel sheet saved to:\n{out_path}")

if __name__ == "__main__":
    main() 