# Gunakan Python slim image untuk ukuran lebih kecil
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir psutil

# Copy aplikasi ke container
COPY app.py .

# Set environment variable
ENV PYTHONUNBUFFERED=1

# Jalankan aplikasi
CMD ["python", "app.py"]