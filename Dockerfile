FROM ubuntu:latest
FROM python:latest
LABEL authors="markus"

ENTRYPOINT ["top", "-b"]

# Dockerfile

# Start from the Python latest image

COPY ./requirements.txt /tmp/requirements.txt
# Copy the rest of your application's code into the container
COPY . /app
WORKDIR /app
EXPOSE 8000
# Install dependencies
COPY requirements.txt ./

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp/

# Run command
CMD [ "python", "-m", "unittest", "discover", "-s", "tests" ]

USER containeruser