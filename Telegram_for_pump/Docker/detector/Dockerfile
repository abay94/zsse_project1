FROM ubuntu:latest
MAINTAINER Abay Aubakirov "a.aubakirov@zeinetsse.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
WORKDIR /usr/local/bin
COPY detector_notificator.py ./
RUN pip install requests
RUN pip install influxdb
ENTRYPOINT ["python"]
CMD ["detector_notificator.py"]
