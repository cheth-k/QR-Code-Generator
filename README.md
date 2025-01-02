# QR Code Generator
- A Python utility for generating customizable QR codes with options for colors, size, and file naming.
## Features
- Generate QR codes from text or URLs.
- Customize QR code colors.
- Adjustable size and border
- Automatic timestamp-based file naming.
- Custom output directory support.
## Requirements
- Python 3.x
- Pillow (PIL)
## Installation
```pip install qrcode pillow```
## Usage
```
from qr_generator import generate_qr

# Basic usage
generate_qr("Hello World")

# Custom settings
generate_qr(
    "https://example.com",
    filename="website_qr.png",
    fill_color="black",
    back_color="white",
    box_size=10,
    border=4
)
```
## Parameters
- ```data```: Text/URL to encode.
- ```output_dir```: Output directory (default: 'QR Code Generator/Generated QRs')
