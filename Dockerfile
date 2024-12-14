# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory to the container
COPY . .

# Salin file model.h5 ke dalam direktori aplikasi
COPY model.h5 /app/model.h5

# Expose the port the app runs on
EXPOSE 5000

# Set the default command to run the app
CMD ["python", "run.py"]
