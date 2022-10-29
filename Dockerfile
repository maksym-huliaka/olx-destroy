#Labels as key value pair
#Deriving the latest base image
FROM python:latest

COPY . /app
WORKDIR /app

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

CMD ["python3", "./source/main.py"]