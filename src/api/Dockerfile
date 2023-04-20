# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r app/requirements.txt

# Expose port 80 for the container
EXPOSE 8111

# Run the command to start FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8111"]
