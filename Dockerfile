FROM ubuntu:latest
#FROM python:latest
LABEL authors="Markus"

# Install python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get install -y python3-venv && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements to app-folder
COPY ./requirements.txt /app/
WORKDIR /app/


# open specified port to the outside
ENV PORT=2000
EXPOSE 2000

# Install dependencies
RUN python3 -m venv /app/venv && \
    /app/venv/bin/pip install --upgrade pip && \
    /app/venv/bin/pip install -r /app/requirements.txt

# Copy SourceCode to app-folder
COPY ../ /app/


## set environment for python-version
ENV PATH="/app/venv/bin:${PATH}"

# setting the user for the container
#USER containeruser

#CMD ["python", "-m", "unittest", "discover", "-s", "", "-p", "*test_*.py"]