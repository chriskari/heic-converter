# HEIC to JPEG Converter

A Python script to batch convert HEIC/HEIF images to JPEG format. The script processes all images from an input folder and saves converted files to an output folder with customizable quality settings. It provides real-time conversion progress and summary statistics, and overwrites existing files by default for convenient re-processing.

## Requirements

- Python 3.6+
- Required packages (see `requirements.txt`):
  - `pillow-heif`
  - `pillow`

## Quick Start

1. **Clone the repository:**

   ```bash
   git clone https://github.com/chriskari/heic-converter.git
   cd heic-converter
   ```

2. **Create and activate virtual environment:**

   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Add your HEIC files:**

   - Place your HEIC/HEIF images in the `input/` folder

5. **Run the converter:**

   ```bash
   python convert.py
   ```

6. **Find converted images:**
   - Your JPEG files will be saved in the `output/` folder

## Usage

### Basic Usage (Default Settings)

```bash
python convert.py
```

This will convert all HEIC/HEIF files from the `input/` folder to the `output/` folder with 90% quality.

### Custom Folders

```bash
python convert.py my_photos converted_photos
```

### Custom Quality

```bash
python convert.py input output 95
```

## Command Line Options

| Argument        | Description                         | Default  |
| --------------- | ----------------------------------- | -------- |
| `input_folder`  | Source folder containing HEIC files | `input`  |
| `output_folder` | Destination folder for JPEG files   | `output` |
| `quality`       | JPEG quality (1-100)                | `90`     |

## Examples

### Convert with High Quality

```bash
python convert.py input output 100
```

### Convert from Custom Folders

```bash
python convert.py "C:/Users/Photos/HEIC" "C:/Users/Photos/Converted" 85
```

## Output

The script provides detailed feedback during conversion:

```
📁 Found 3 HEIC/HEIF files in input
📁 Output folder: output
--------------------------------------------------
✅ Successfully converted: IMG_5716.HEIC → IMG_5716.jpg
✅ Successfully converted: IMG_5720.HEIC → IMG_5720.jpg
✅ Successfully converted: IMG_5721.HEIC → IMG_5721.jpg
--------------------------------------------------
📊 Conversion Summary:
   ✅ Successful: 3
   ❌ Failed: 0
   📄 Total files: 3
```

## Supported Formats

- **Input**: `.heic`, `.heif` (case-insensitive)
- **Output**: `.jpg` (JPEG format)
