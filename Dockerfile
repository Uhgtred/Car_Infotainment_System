FROM ubuntu:latest
LABEL authors="markus"

ENTRYPOINT ["top", "-b"]

# Dockerfile

# Start from the Python latest image
FROM python:3.10

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./Car_Infotainment_System /Car_Infotainment_System
WORKDIR /app
EXPOSE 8000
# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code into the container
COPY . /app

# Run command
CMD [ "python", "-m", "unittest", "discover", "-s", "tests" ]