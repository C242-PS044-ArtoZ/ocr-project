# Gunakan base image Python yang ringan
FROM python:3.9-slim

# Install Tesseract OCR dan dependensi lainnya
RUN apt-get update && apt-get install -y tesseract-ocr libtesseract-dev

# Set working directory dalam container
WORKDIR /app

# Copy semua file proyek ke dalam container
COPY . /app

# Install Python dependencies dari requirements.txt
RUN pip install -r app/requirements.txt

# Expose port 5000 untuk Flask
EXPOSE 5000

# Jalankan aplikasi Flask
CMD ["python", "app/main.py"]
