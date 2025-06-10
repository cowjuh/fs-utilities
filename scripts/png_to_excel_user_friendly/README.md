# PNG to Excel Converter

This tool converts all PNG images in a selected folder into an Excel file with thumbnails and metadata.

## Requirements
- Python 3.9 or newer (install from https://www.python.org if needed)
- pip (Python package manager)

## Installing Python and pip on macOS

If you don't have Python 3.9+ and pip installed, follow these steps:

### 1. Install Homebrew (if you don't have it)
Homebrew is a popular package manager for macOS. Open Terminal and run:
```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2. Install Python (includes pip)
With Homebrew installed, run:
```sh
brew install python
```
This will install the latest version of Python 3 and pip.

### 3. Verify Installation
Check that Python 3 and pip are installed:
```sh
python3 --version
pip3 --version
```
You should see Python 3.9 or newer and a pip version.

If you have any issues, visit the [official Python installation guide](https://docs.python.org/3/using/mac.html) or [Homebrew documentation](https://brew.sh/).

## Setup
1. Open Terminal.
2. Navigate to this folder. For example:
   ```sh
   cd /Users/cowjuh/Documents/scripts/png_to_excel_user_friendly
   ```
3. Install the required Python packages:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. In Terminal, run:
   ```sh
   python3 png_to_excel_user_friendly.py
   ```
2. A window will appear asking you to select the folder containing your PNG files.
3. The script will create a new folder next to your images with an Excel file containing thumbnails and image information.

If you have any issues, ensure you are using Python 3.9+ and that all dependencies are installed. 