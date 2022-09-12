FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y python3 python3-pip
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT FLASK_APP=/app/app.py flask run --host=0.0.0.0 --port=5000