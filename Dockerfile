FROM ubuntu:latest
FROM python:latest
LABEL authors="Markus"

# Copy requirements to app-folder
COPY requirements.txt /app/
WORKDIR /app/


# open specified port to the outside
ENV PORT=2000
EXPOSE 2000

# Install dependencies
RUN python -m venv /app/ && \
    source /app/bin/activate && \
    /app/bin/pip install --upgrade pip && \
    ls /app/ && \
    /app/bin/pip install -r /app/requirements.txt

# Copy SourceCode to app-folder
COPY . /app/


## set environment for python-version
ENV PYTHONPATH = "/app/"

# setting the user for the container
#USER containeruser

#CMD ["python", "-m", "unittest", "discover", "-s", "", "-p", "*test_*.py"]