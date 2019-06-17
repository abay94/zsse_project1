FROM ubuntu:latest
MAINTAINER Abay Aubakirov "a.aubakirov@zeinetsse.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
WORKDIR /usr/local/bin
COPY telegram_bot.py ./
RUN pip install requests
RUN pip install influxdb
RUN pip install pytelegrambotapi
ENTRYPOINT ["python"]
CMD ["telegram_bot.py"]