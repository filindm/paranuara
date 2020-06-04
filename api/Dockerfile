FROM python:3.8.3-buster

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000

CMD FLASK_APP=paranuara flask run --host=0.0.0.0
