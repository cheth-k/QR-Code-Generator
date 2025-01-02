import qrcode
from PIL import Image
import os
from datetime import datetime

def generate_qr(data, output_dir='QR Code Generator/Generated QRs', filename=None, fill_color='black', back_color='white', box_size=10, border=4):
    """
    Generate a QR code and save it to a specified directory
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate default filename if none provided
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"qr_{timestamp}.png"
    
    # Ensure filename has .png extension
    if not filename.endswith('.png'):
        filename += '.png'
    
    # Create full file path
    filepath = os.path.join(output_dir, filename)
    
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    
    # Add data and generate QR code
    qr.add_data(data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color=fill_color, back_color=back_color)
    
    # Save the image
    qr_image.save(filepath)
    return filepath

# Example usage
if __name__ == "__main__":
    # Generate QR codes with default and custom settings
    generate_qr("Example")
    generate_qr(
        "https://example.com/",
        filename="Example.com.png",
        fill_color="Black",
        back_color="White"
        #box_size=15,
        #border=5
    )