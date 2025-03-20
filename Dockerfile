# Use the official Python image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy only requirements file first (for better Docker caching)
COPY backend/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY backend/ .

# Expose port 5000 for Flask
EXPOSE 5000

# Start the Flask app using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "main:app"]
