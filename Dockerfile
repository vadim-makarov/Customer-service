FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y python3.11
RUN apt-get install -y python3-pip
RUN apt pip install --upgrade pip
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT FLASK_APP=/app/app.py flask run --host=0.0.0.0 --port=5000