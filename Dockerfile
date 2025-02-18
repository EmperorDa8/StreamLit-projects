# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

# Install any dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Specify the Streamlit port explicitly (Cloud Run requires this)
ENV PORT=8080

# Command to run the Streamlit app, binding to the $PORT environment variable
CMD streamlit run main.py --server.port $PORT --server.enableCORS false
