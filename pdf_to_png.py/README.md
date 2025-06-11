# PDF to PNG Converter

A simple Python utility that converts PDF files to PNG images, with each page saved as a separate PNG file.

## Requirements

- Python 3.x
- pdf2image==1.16.3
- Pillow==10.2.0

## Installation

1. Clone this repository or download the files
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

Note: This utility requires `poppler` to be installed on your system:
- **macOS**: `brew install poppler`
- **Ubuntu/Debian**: `apt-get install poppler-utils`
- **Windows**: Download and install poppler from [poppler for Windows](http://blog.alivate.com.au/poppler-windows/)

## Usage

Run the script from the command line, providing the path to your PDF file:

```bash
python pdf_to_png.py path/to/your/file.pdf
```

The script will:
1. Create a new directory named `{filename}_pngs` in the same location as your PDF
2. Convert each page of the PDF to a PNG image
3. Save the images as `page_001.png`, `page_002.png`, etc.

## Output

- Images are saved in a new directory named after your PDF file (with `_pngs` suffix)
- Each page is saved as a separate PNG file
- Files are numbered sequentially (e.g., page_001.png, page_002.png, etc.)

## Example

```bash
python pdf_to_png.py document.pdf
```

This will create a directory named `document_pngs` containing all the converted PNG images. 