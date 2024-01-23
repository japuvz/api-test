# Use the official Python base image
FROM python:3.12-slim
#FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory
COPY ./app .

# Expose the port on which the FastAPI application will run
EXPOSE 8000

# Start the FastAPI application with reload option
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
