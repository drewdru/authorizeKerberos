FROM debian:9.4
USER root
RUN mkdir /code
WORKDIR /code
ADD . /code/
