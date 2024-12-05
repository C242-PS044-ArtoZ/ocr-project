from flask import Flask, request, jsonify
from ocr_utils import extract_text_from_image, extract_total_amount
from preprocess_utils import preprocess_image
import os

# Inisialisasi Flask App
app = Flask(__name__)

# Endpoint untuk upload gambar dan OCR
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    file_path = os.path.join("uploads", file.filename)
    file.save(file_path)

    # Praproses gambar
    processed_image_path = preprocess_image(file_path)

    # OCR pada gambar yang sudah diproses
    ocr_result = extract_text_from_image(processed_image_path)
    total_amount = extract_total_amount(ocr_result)
    os.remove(file_path)
    os.remove(processed_image_path)

    return jsonify({"ocr_text": ocr_result, "total_amount": total_amount})

if __name__ == '__main__':
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
    app.run(host='0.0.0.0', port=5000)
