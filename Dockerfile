FROM ubuntu:latest
FROM python:latest
LABEL authors="markus"

ENTRYPOINT ["top", "-b"]

# Dockerfile

# Copy application's code into the container
COPY . /app
WORKDIR /app
EXPOSE 8000

# set environment for python-version
ENV PATH = "/py/bin:$PATH"

## Install dependencies
RUN py/bin/pip install virtualenv && \
    python -m venv /py/venv && \
    /py/python venv/Scripts/activate && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r requirements.txt && \
    adduser --disabled-password --no-create-home containeruser

# setting the user for the container
USER containeruser