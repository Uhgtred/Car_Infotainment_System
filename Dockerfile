FROM ubuntu:latest
LABEL authors="markus"

ENTRYPOINT ["top", "-b"]

# Dockerfile

# Start from the Python latest image
FROM python:3.10

COPY ./requirements.txt /tmp/requirements.txt
# Copy the rest of your application's code into the container
COPY . /app
WORKDIR /app
EXPOSE 8000
# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt \
    adduser --disabled-password --no-create-home containeruser

# Run command
CMD [ "python", "-m", "unittest", "discover", "-s", "tests" ]

USER containeruser