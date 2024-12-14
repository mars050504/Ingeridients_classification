# Gunakan image dasar Python
FROM python:3.9-slim

# Set working directory di dalam container
WORKDIR /app

# Copy file requirements.txt ke dalam container
COPY requirements.txt /app/

# Install dependensi yang ada di requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Salin semua file aplikasi ke dalam container
COPY . /app/

# Set port yang akan digunakan oleh aplikasi Flask
EXPOSE 8080

# Tentukan command untuk menjalankan aplikasi
CMD ["python", "app.py"]
