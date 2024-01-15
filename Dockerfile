FROM ubuntu:latest
FROM python:latest
LABEL authors="markus"

ENTRYPOINT ["top", "-b"]

# Dockerfile

# Copy application's code into the container
COPY . /app
WORKDIR /app
EXPOSE 8000

## Install dependencies
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r requirements.txt && \
    rm -rf /tmp/

# set environment for python-version
ENV PATH = "/py/bin:$PATH"

# setting the user for the container
USER containeruser