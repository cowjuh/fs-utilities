#!/usr/bin/env python3

import os
from pdf2image import convert_from_path
import sys

def convert_pdf_to_png(pdf_path):
    # Get the directory and filename without extension
    directory = os.path.dirname(pdf_path)
    filename = os.path.splitext(os.path.basename(pdf_path))[0]
    
    # Create output directory
    output_dir = os.path.join(directory, f"{filename}_pngs")
    os.makedirs(output_dir, exist_ok=True)
    
    # Convert PDF to images
    print(f"Converting {pdf_path} to PNG images...")
    images = convert_from_path(pdf_path)
    
    # Save each page as PNG
    for i, image in enumerate(images):
        output_path = os.path.join(output_dir, f"page_{i+1:03d}.png")
        image.save(output_path, "PNG")
        print(f"Saved page {i+1} to {output_path}")
    
    print(f"\nConversion complete! {len(images)} pages converted.")
    print(f"Images saved in: {output_dir}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pdf_to_png.py <path_to_pdf>")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    if not os.path.exists(pdf_path):
        print(f"Error: File {pdf_path} does not exist")
        sys.exit(1)
    
    convert_pdf_to_png(pdf_path) 