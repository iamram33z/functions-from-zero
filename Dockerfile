# Use the official Python image with version 3.12
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .

# Upgrade pip and install requirements
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the rest of your application code
COPY . .

# Set environment variables to disable buffering for better logging
ENV PYTHONUNBUFFERED=1

# Install additional tools (like black and pylint)
RUN pip install black pylint pytest

# Default command when running the container (can be overridden)
CMD ["bash"]
