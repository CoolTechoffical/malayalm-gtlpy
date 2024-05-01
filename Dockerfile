# Use a Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Install required system dependencies
RUN apt-get update && \
    apt-get install -y \
    libmagic1 \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the Python dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script into the container
COPY malayalam_chatgpt_bot.py .

# Run the Python script
CMD ["python", "malayalam_chatgpt_bot.py"]
