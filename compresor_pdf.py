#!/usr/bin/env python3
# Author: Theeko74
# Contributor(s): skjerns
# Oct, 2021
# MIT license -- free to use as you want, cheers.

"""
Simple python wrapper script to use ghoscript function to compress PDF files.

Compression levels:
    0: default - almost identical to /screen, 72 dpi images
    1: prepress - high quality, color preserving, 300 dpi imgs
    2: printer - high quality, 300 dpi images
    3: ebook - low quality, 150 dpi images
    4: screen - screen-view-only quality, 72 dpi images

Dependency: Ghostscript.
On MacOSX install via command line `brew install ghostscript`.
"""

import os.path
import shutil
import subprocess
import sys

def format_size(size):
    # Convertir bytes a kilobytes (KB), megabytes (MB) o gigabytes (GB)
    if size < 1024:
        return "{:.2f} bytes".format(size)
    elif size < 1024 * 1024:
        return "{:.2f} KB".format(size / 1024)
    elif size < 1024 * 1024 * 1024:
        return "{:.2f} MB".format(size / (1024 * 1024))
    else:
        return "{:.2f} GB".format(size / (1024 * 1024 * 1024))


def compress(input_file_path, output_file_path, power=0):
    """Function to compress PDF via Ghostscript command line interface"""
    quality = {
        0: "/default",
        1: "/prepress",
        2: "/printer",
        3: "/ebook",
        4: "/screen"
    }

    # Basic controls
    # Check if valid path
    if not os.path.isfile(input_file_path):
        print("Error: invalid path for input PDF file.", input_file_path)
        sys.exit(1)

    # Check compression level
    if power < 0 or power > len(quality) - 1:
        print("Error: invalid compression level, run pdfc -h for options.", power)
        sys.exit(1)

    # Check if file is a PDF by extension
    if input_file_path.split('.')[-1].lower() != 'pdf':
        print(f"Error: input file is not a PDF.", input_file_path)
        sys.exit(1)

    gs = get_ghostscript_path()
    print("Compress PDF...")
    initial_size = os.path.getsize(input_file_path)
    subprocess.call(
        [
            gs,
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.4",
            "-dPDFSETTINGS={}".format(quality[power]),
            "-dNOPAUSE",
            "-dQUIET",
            "-dBATCH",
            "-sOutputFile={}".format(output_file_path),
            input_file_path,
        ]
    )
    final_size = os.path.getsize(output_file_path)
    formatted_size = format_size(final_size)
    ratio = 1 - (final_size / initial_size)
    print("Compression by {0:.0%}.".format(ratio))
    print("Final file size is", formatted_size)
    print("Done.")


def get_ghostscript_path():
    gs_names = [
        "/usr/bin/gs",  # Linux default path
        "c:\Program Files\gs\gs10.03.0\\bin\gswin64.exe"  # Windows default path
    ]
    for name in gs_names:
        if shutil.which(name):
            return shutil.which(name)
    raise FileNotFoundError(
        f"No GhostScript executable was found on path ({'/'.join(gs_names)})"
    )


def main():
    print("Welcome to PDF Compressor!")
    input_file_path = input("Enter the path of the input PDF file: ").strip()
    output_file_path = input("Enter the path of the output PDF file (leave blank for default): ").strip()
    compress_level = int(input("Enter compression level (0 to 4, default is 2): ").strip() or "2")

    # Run
    compress(input_file_path, output_file_path, power=compress_level)

    # In case no output file is specified, erase original file
    if not output_file_path:
        if input("Do you want to create a backup of the original file? (yes/no): ").strip().lower() == "yes":
            shutil.copyfile(input_file_path, input_file_path.replace(".pdf", "_BACKUP.pdf"))
        shutil.copyfile("temp.pdf", input_file_path)
        os.remove("temp.pdf")

    # In case we want to open the file after compression
    if input("Do you want to open the compressed PDF? (yes/no): ").strip().lower() == "yes":
        if not output_file_path and input("Do you want to open the original or the compressed PDF? (original/compressed): ").strip().lower() == "original":
            os.startfile(input_file_path)
        else:
            os.startfile(output_file_path or "temp.pdf")

if __name__ == "__main__":
    main()