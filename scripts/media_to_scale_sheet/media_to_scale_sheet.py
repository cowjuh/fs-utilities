#!/usr/bin/env python3
"""
Media to Scale Sheet Converter for Figma
=======================================

This script converts images and PDFs in a specified folder into SVG files
that can be directly pasted into Figma, maintaining relative scaling
and including dimension information as an overlay.

Usage:
    python3 media_to_scale_sheet.py -i /path/to/input/folder -o /path/to/output/folder

Options:
    -i, --input     Path to the folder containing media files (required)
    -o, --output    Path to the output folder (required)

Requirements:
- Python 3.9+
- Pillow
- pdf2image
- poppler-utils (system dependency)
- base64
"""
import os
import sys
import argparse
import base64
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from pdf2image import convert_from_path

# Supported file extensions
SUPPORTED_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.tif', '.tiff', '.pdf'}

# Figma's maximum dimension
FIGMA_MAX_DIMENSION = 4096

def calculate_scaled_dimensions(w, h, target_w, target_h):
    """Calculate dimensions that fit within Figma's limits while maintaining aspect ratio."""
    # Calculate aspect ratio
    aspect_ratio = w / h
    
    # Calculate dimensions that maintain aspect ratio
    if target_w / target_h > aspect_ratio:
        # Height is the limiting factor
        new_h = target_h
        new_w = int(new_h * aspect_ratio)
    else:
        # Width is the limiting factor
        new_w = target_w
        new_h = int(new_w / aspect_ratio)
    
    return new_w, new_h

def get_global_scaling_factor(media_files, input_dir):
    """Calculate a single scaling factor that works for all images."""
    max_target_w = 0
    max_target_h = 0
    
    for fname in media_files:
        path = os.path.join(input_dir, fname)
        try:
            img = Image.open(path)
            # Process orientation BEFORE getting dimensions
            img = process_image(img)
            w, h = img.size
            w_in = w / 300  # Convert to inches at 300 DPI
            h_in = h / 300
            
            # Calculate target dimensions for Figma (96 DPI)
            target_w = int(w_in * 96)
            target_h = int(h_in * 96)
            
            max_target_w = max(max_target_w, target_w)
            max_target_h = max(max_target_h, target_h)
        except Exception as e:
            print(f"Warning: Could not process {fname} for scaling calculation: {e}")
            continue
    
    if max_target_w <= FIGMA_MAX_DIMENSION and max_target_h <= FIGMA_MAX_DIMENSION:
        return 1.0
    
    return min(FIGMA_MAX_DIMENSION / max_target_w, FIGMA_MAX_DIMENSION / max_target_h)

def image_to_base64(img):
    """Convert PIL Image to base64 string."""
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

def create_svg(img_info, img_data, font_size=18):
    """Create SVG with embedded image and overlay text."""
    w = img_info['w_figma']
    h = img_info['h_figma']
    
    # Calculate responsive font sizes based on image dimensions
    base_font_size = min(max(min(w, h) // 10, 48), 96)  # Scale between 48-96 based on image size
    small_font_size = max(base_font_size - 48, 48)  # Smaller text but not below 48
    
    # Gap between image and bottom text
    gap = 50
    
    # Create SVG with embedded image and overlay
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{w}" height="{h + 200 + gap}" viewBox="0 0 {w} {h + 200 + gap}" xmlns="http://www.w3.org/2000/svg">
    <!-- Background Image -->
    <image width="{w}" height="{h}" href="data:image/png;base64,{img_data}"/>
    
    <!-- Top Overlay Group -->
    <g id="TOP_METADATA_{img_info['fname']}">
        <!-- Overlay Background -->
        <rect width="{w}" height="200" fill="rgba(0,0,0,0.7)"/>
        
        <!-- Filename -->
        <text x="20" y="70" fill="white" font-family="Arial" font-size="{base_font_size}">
            {img_info['fname']}
        </text>
        
        <!-- Folder -->
        <text x="20" y="120" fill="white" font-family="Arial" font-size="{small_font_size}">
            Folder: {img_info['folder']}
        </text>
        
        <!-- Original Dimensions -->
        <text x="20" y="170" fill="white" font-family="Arial" font-size="{small_font_size}">
            Original: {img_info['w_original']}x{img_info['h_original']} px | {img_info['w_in']:.2f}in x {img_info['h_in']:.2f}in
        </text>
    </g>

    <!-- Bottom Metadata Group -->
    <g id="BOTTOM_METADATA_{img_info['fname']}" transform="translate(0, {h + gap})">
        <!-- Filename -->
        <text x="20" y="70" fill="black" font-family="Arial" font-size="{base_font_size}">
            {img_info['fname']}
        </text>
        
        <!-- Folder -->
        <text x="20" y="120" fill="black" font-family="Arial" font-size="{small_font_size}">
            Folder: {img_info['folder']}
        </text>
        
        <!-- Original Dimensions -->
        <text x="20" y="170" fill="black" font-family="Arial" font-size="{small_font_size}">
            Original: {img_info['w_original']}x{img_info['h_original']} px | {img_info['w_in']:.2f}in x {img_info['h_in']:.2f}in
        </text>
    </g>
</svg>'''
    return svg

def convert_pdf_to_images(pdf_path, output_dir):
    """Convert first page of PDF to PNG image and return the generated filename."""
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    # Only convert first page
    images = convert_from_path(pdf_path, dpi=300, first_page=1, last_page=1)
    
    if not images:
        return None
        
    # Save the original PDF page as PNG
    temp_output_name = f"{base_name}_first_page.png"
    temp_output_path = os.path.join(output_dir, temp_output_name)
    images[0].save(temp_output_path, "PNG")
    
    return temp_output_name, temp_output_path  # Return both name and path for cleanup

def process_image(img):
    """Process image to handle orientation and return properly oriented image."""
    try:
        # Check if image has EXIF data
        if hasattr(img, '_getexif') and img._getexif() is not None:
            exif = img._getexif()
            if exif is not None:
                # Get orientation tag
                orientation = exif.get(274)  # 274 is the orientation tag
                if orientation is not None:
                    # Rotate image based on orientation
                    if orientation == 3:
                        img = img.rotate(180, expand=True)
                    elif orientation == 6:
                        img = img.rotate(270, expand=True)
                    elif orientation == 8:
                        img = img.rotate(90, expand=True)
        
        # Handle TIFF orientation
        if hasattr(img, 'tag') and hasattr(img.tag, 'get'):
            tiff_orientation = img.tag.get(274)  # TIFF orientation tag
            if tiff_orientation is not None:
                if tiff_orientation == 8:  # LeftBottom
                    img = img.rotate(90, expand=True)
                elif tiff_orientation == 3:  # BottomRight
                    img = img.rotate(180, expand=True)
                elif tiff_orientation == 6:  # RightTop
                    img = img.rotate(270, expand=True)
    except Exception as e:
        print(f"Warning: Could not process image orientation: {e}")
    return img

def main():
    # Set up command line arguments
    parser = argparse.ArgumentParser(description='Convert media files to Figma-compatible SVGs.')
    parser.add_argument('-i', '--input', required=True, help='Path to the folder containing media files')
    parser.add_argument('-o', '--output', required=True, help='Path to the output folder')
    args = parser.parse_args()

    # Get input and output directories
    input_dir = args.input
    output_dir = args.output

    # Check if input directory exists
    if not os.path.isdir(input_dir):
        print(f"Error: Input directory '{input_dir}' is not a valid directory")
        sys.exit(1)

    # Create output directory
    try:
        os.makedirs(output_dir, exist_ok=True)
    except Exception as e:
        print(f"Error creating output directory: {e}")
        sys.exit(1)

    # Gather all supported files
    media_files = [f for f in os.listdir(input_dir) 
                  if os.path.splitext(f)[1].lower() in SUPPORTED_EXTENSIONS]
    
    if not media_files:
        print(f"No supported files found in '{input_dir}'")
        print(f"Supported extensions: {', '.join(SUPPORTED_EXTENSIONS)}")
        sys.exit(0)

    # Process PDFs first and add generated PNGs to the list
    pdf_files = [f for f in media_files if f.lower().endswith('.pdf')]
    temp_files = []  # Keep track of temporary files for cleanup
    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_dir, pdf_file)
        try:
            print(f"Converting first page of PDF: {pdf_file}")
            result = convert_pdf_to_images(pdf_path, output_dir)
            if result:
                generated_file, temp_path = result
                media_files.extend([generated_file])
                temp_files.append(temp_path)  # Add to cleanup list
            media_files.remove(pdf_file)
        except Exception as e:
            print(f"Error converting PDF {pdf_file}: {e}")
            continue

    print(f"Processing {len(media_files)} files...")
    print("Note: All images will be scaled to 10px per inch for consistency")

    # Process images and calculate dimensions
    for fname in media_files:
        # Determine the correct path based on whether it's a PDF-generated file or original file
        if fname.endswith('_first_page.png'):
            path = os.path.join(output_dir, fname)
            original_name = fname.replace('_first_page.png', '.pdf')
        else:
            path = os.path.join(input_dir, fname)
            original_name = fname
            
        try:
            # Open and process orientation first
            img = Image.open(path)
            img = process_image(img)
            
            # Get dimensions AFTER orientation processing
            w_original, h_original = img.size
            
            # Calculate physical dimensions in inches (at 300 DPI)
            w_in = w_original / 300
            h_in = h_original / 300
            
            # Calculate target dimensions for Figma (100 pixels per inch)
            target_w = int(w_in * 100)
            target_h = int(h_in * 100)
            
            # Debug output
            print(f"  After orientation: {w_original}×{h_original} px")
            print(f"  Physical size: {w_in:.2f}×{h_in:.2f} inches")
            print(f"  Target Figma size (100px per inch): {target_w}×{target_h} px")
            
            # Calculate scaled dimensions that maintain aspect ratio
            w_figma, h_figma = calculate_scaled_dimensions(w_original, h_original, target_w, target_h)
            
            print(f"  Final Figma size: {w_figma}×{h_figma} px")
            
            # Resize to target dimensions using thumbnail to maintain aspect ratio
            img.thumbnail((w_figma, h_figma), Image.LANCZOS)
            
            # Get final dimensions after resizing
            w_final, h_final = img.size
            
            # Convert image to base64
            img_data = image_to_base64(img)
            
            # Create image info dictionary with post-rotation dimensions
            img_info = {
                'fname': original_name,
                'w_figma': w_final,
                'h_figma': h_final,
                'w': w_final,
                'h': h_final,
                'w_original': w_original,  # These are now the post-rotation dimensions
                'h_original': h_original,  # These are now the post-rotation dimensions
                'w_in': w_in,
                'h_in': h_in,
                'folder': os.path.basename(input_dir)
            }
            
            # Create SVG
            svg_content = create_svg(img_info, img_data)
            
            # Save SVG file
            output_name = os.path.splitext(original_name)[0] + '_figma.svg'
            output_path = os.path.join(output_dir, output_name)
            with open(output_path, 'w') as f:
                f.write(svg_content)
            print(f"Saved: {output_path}")
            
        except Exception as e:
            print(f"Skipping {fname}: {e}")
            continue

    # Clean up all temporary files
    for temp_file in temp_files:
        try:
            if os.path.exists(temp_file):
                os.remove(temp_file)
                print(f"Cleaned up temporary file: {temp_file}")
        except Exception as e:
            print(f"Warning: Could not remove temporary file {temp_file}: {e}")

    print("\nDone! All images have been converted to Figma-compatible SVGs.")
    print("You can now copy and paste these SVGs directly into Figma.")
    print("The dimension information is overlaid on a semi-transparent black background.")

if __name__ == "__main__":
    main()