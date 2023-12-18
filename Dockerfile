FROM ubuntu:latest
LABEL authors="markus"

ENTRYPOINT ["top", "-b"]

# Dockerfile

# Start from the Python latest image
FROM python:latest

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code into the container
COPY . /app

# Run command
CMD [ "python", "-m", "unittest", "discover", "-s", "tests" ]