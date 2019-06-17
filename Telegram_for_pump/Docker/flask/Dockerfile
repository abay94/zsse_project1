FROM ubuntu:latest
MAINTAINER Abay Aubakirov "a.aubakirov@zeinetsse.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
WORKDIR /usr/local/bin
COPY flask_server.py ./
RUN pip install flask==0.12.2  
RUN pip install requests
RUN pip install influxdb
ENTRYPOINT ["python"]
CMD ["flask_server.py"]

