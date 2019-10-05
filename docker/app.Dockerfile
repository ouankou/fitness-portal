FROM ubuntu:18.04

RUN apt update
RUN apt install -y \
    curl \
    python3-pip \
    mysql-server \
    python-dev \
    libmysqlclient-dev

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

#RUN mkdir /fitness-portal
#WORKDIR /fitness-portal
#COPY ../../fitness-portal /fitness-portal

#RUN adduser -D user
#USER user
COPY ./start.sh /start.sh
CMD ["bash", "/start.sh"]