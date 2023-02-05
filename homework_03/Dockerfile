##for start container make image for this container
#docker build . -t app
##then check image
#docker images
##then start conteiner based on this image
#docker run -it -p 8080:8000 app
##then try open app in web 127.0.0.1/8080/ping

FROM python:3.9-buster

WORKDIR /var/app

COPY . .
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8000

CMD uvicorn --host 0.0.0.0 main:app
#CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
