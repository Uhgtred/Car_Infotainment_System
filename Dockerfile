FROM ubuntu:latest
FROM python:latest
LABEL authors="Markus"

# Copy requirements to app-folder
#COPY requirements.txt /app/

# open specified port to the outside
ENV PORT=2000
EXPOSE 2000

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy SourceCode to app-folder
COPY . /app/
WORKDIR /app/

## set environment for python-version
#ENV PATH = "$PATH:/app/"

# setting the user for the container
#USER containeruser

#CMD ["python", "-m", "unittest", "discover", "-s", "", "-p", "*test_*.py"]