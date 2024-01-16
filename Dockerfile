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
RUN python -m venv /venv && \
#    /py/venv/Scripts/activate && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r requirements.txt && \
    adduser --disabled-password --no-create-home containeruser

# setting the user for the container
USER containeruser