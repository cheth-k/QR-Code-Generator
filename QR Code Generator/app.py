from flask import Flask, render_template, request, send_file, jsonify
import os
from datetime import datetime
import qrcode
from PIL import Image

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = os.path.join('static', 'Generated QRs')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def generate_qr(data, filename=None, fill_color='black', back_color='white', box_size=10, border=4):
    """
    Generate a QR code and save it to the static folder
    """
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"qr_{timestamp}.png"
    
    if not filename.endswith('.png'):
        filename += '.png'
    
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    
    qr.add_data(data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color=fill_color, back_color=back_color)
    
    qr_image.save(filepath)
    return filename

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.form.get('data')
    fill_color = request.form.get('fill_color', 'black')
    back_color = request.form.get('back_color', 'white')
    box_size = int(request.form.get('box_size', 10))
    border = int(request.form.get('border', 4))
    
    filename = generate_qr(
        data,
        fill_color=fill_color,
        back_color=back_color,
        box_size=box_size,
        border=border
    )
    
    return jsonify({
        'success': True,
        'filename': filename,
        'filepath': f'Generated QRs/{filename}'
    })

if __name__ == '__main__':
    app.run(debug=True)