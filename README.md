# QR Code Generator Web Application

A web-based QR code generator built with Flask, HTML, CSS, and JavaScript. This application allows users to generate customized QR codes from text or URLs with various styling options.

## Features

- Generate QR codes from text or URLs
- Customize QR code appearance:
  - QR code color
  - Background color
  - Size adjustment
  - Border width control
- Real-time preview
- Download generated QR codes
- Responsive web interface

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/qr-code-generator.git
cd qr-code-generator
```

2. Create and activate a virtual environment (recommended):
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install required packages:
```bash
pip install flask qrcode pillow
```

## Project Structure

```
QR Code Generator/
├── app.py                 # Flask application
├── static/
│   ├── css/
│   │   └── style.css     # Stylesheet
│   └── Generated QRs/    # Generated QR codes storage
└── templates/
    └── index.html        # Main webpage template
```

## Usage

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://127.0.0.1:5000
```

3. To generate a QR code:
   - Enter text or URL in the input field
   - Customize appearance using the color pickers and sliders
   - Click "Generate QR Code"
   - Use the "Download" button to save the generated QR code

## Configuration Options

- **QR Code Color**: Choose any color for the QR code pattern
- **Background Color**: Select the QR code's background color
- **Size**: Adjust the QR code size (5-20)
- **Border Width**: Modify the quiet zone around the QR code (1-10)

## Dependencies

- Flask: Web framework
- qrcode: QR code generation library
- Pillow: Python Imaging Library for image processing

## Development

To modify the application:
- Edit `app.py` for backend logic
- Modify `templates/index.html` for frontend changes
- Update `static/css/style.css` for styling adjustments

## Browser Compatibility

Tested and working on:
- Google Chrome
- Mozilla Firefox
- Microsoft Edge
- Safari

## Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m 'Add YourFeature'`
4. Push to the branch: `git push origin feature/YourFeature`
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

[Your Name]

## Acknowledgments

- [qrcode](https://github.com/lincolnloop/python-qrcode) library
- Flask framework
- Contributors and testers
