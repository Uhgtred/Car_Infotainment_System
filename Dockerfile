FROM ubuntu:latest
FROM python:latest
LABEL authors="markus"

ENTRYPOINT ["top", "-b"]

# Dockerfile

# Copy application's code into the container
COPY . /app
WORKDIR /app
EXPOSE 2000

## Install dependencies
RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r requirements.txt && \
    adduser --disabled-password --no-create-home containeruser

# set environment for python-version
ENV PATH = "/py/bin:$PATH"

# setting the user for the container
USER containeruser