"""
Batch HEIC to JPEG converter script
Converts all HEIC files from 'input' folder to 'output' folder
Requires: pillow-heif library
Install with: pip install pillow-heif pillow
"""

import sys
from pathlib import Path
from PIL import Image
import pillow_heif


def convert_heic_to_jpg(input_path, output_path, quality=90):
    """
    Convert HEIC file to JPEG

    Args:
        input_path (Path): Path to input HEIC file
        output_path (Path): Path for output JPEG file
        quality (int): JPEG quality (1-100, default 90)

    Returns:
        bool: True if conversion successful, False otherwise
    """
    try:
        # Open and convert the HEIC image
        with Image.open(input_path) as img:
            # Convert to RGB if necessary (HEIC can have different color modes)
            if img.mode != "RGB":
                img = img.convert("RGB")

            # Save as JPEG
            img.save(output_path, "JPEG", quality=quality)

        print(f"✅ Successfully converted: {input_path.name} → {output_path.name}")
        return True

    except Exception as e:
        print(f"❌ Error converting {input_path.name}: {str(e)}")
        return False


def batch_convert_heic_to_jpg(input_folder="input", output_folder="output", quality=90):
    """
    Convert all HEIC files from input folder to output folder

    Args:
        input_folder (str): Input folder path (default: "input")
        output_folder (str): Output folder path (default: "output")
        quality (int): JPEG quality (1-100, default 90)

    Returns:
        tuple: (successful_conversions, failed_conversions, total_files)
    """
    # Register HEIF opener with Pillow
    pillow_heif.register_heif_opener()

    input_path = Path(input_folder)
    output_path = Path(output_folder)

    # Check if input folder exists
    if not input_path.exists():
        raise FileNotFoundError(f"Input folder not found: {input_path}")

    if not input_path.is_dir():
        raise NotADirectoryError(f"Input path is not a directory: {input_path}")

    # Create output folder if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)

    # Find all HEIC/HEIF files in input folder (case-insensitive)
    heic_files = []
    for file in input_path.iterdir():
        if file.is_file() and file.suffix.lower() in [".heic", ".heif"]:
            heic_files.append(file)

    if not heic_files:
        print(f"⚠️  No HEIC/HEIF files found in {input_folder}")
        return 0, 0, 0

    print(f"📁 Found {len(heic_files)} HEIC/HEIF files in {input_folder}")
    print(f"📁 Output folder: {output_folder}")
    print("-" * 60)

    successful = 0
    failed = 0

    # Convert each file
    for heic_file in heic_files:
        # Generate output filename (same name but with .jpg extension)
        jpg_filename = heic_file.stem + ".jpg"
        jpg_path = output_path / jpg_filename

        if convert_heic_to_jpg(heic_file, jpg_path, quality):
            successful += 1
        else:
            failed += 1

    print("-" * 60)
    print(f"📊 Conversion Summary:")
    print(f"   ✅ Successful: {successful}")
    print(f"   ❌ Failed: {failed}")
    print(f"   📄 Total files: {len(heic_files)}")

    return failed


def main():
    """Main function to handle command line usage"""
    # Default values
    input_folder = "input"
    output_folder = "output"
    quality = 90

    # Parse command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] in ["-h", "--help"]:
            print(
                "Usage: python batch_heic_converter.py [input_folder] [output_folder] [quality]"
            )
            print("Example: python batch_heic_converter.py")
            print(
                "Example: python batch_heic_converter.py my_photos converted_photos 95"
            )
            print("Example: python batch_heic_converter.py input output 85")
            print("\nDefault values:")
            print("  input_folder: 'input'")
            print("  output_folder: 'output'")
            print("  quality: 90")
            return

        input_folder = sys.argv[1]

    if len(sys.argv) > 2:
        output_folder = sys.argv[2]

    if len(sys.argv) > 3:
        try:
            quality = int(sys.argv[3])
            if not 1 <= quality <= 100:
                print("❌ Quality must be between 1 and 100")
                sys.exit(1)
        except ValueError:
            print("❌ Quality must be a valid integer")
            sys.exit(1)

    try:
        failed = batch_convert_heic_to_jpg(input_folder, output_folder, quality)

        if failed > 0:
            sys.exit(1)  # Exit with error code if any conversions failed

    except Exception as e:
        print(f"❌ Batch conversion failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
