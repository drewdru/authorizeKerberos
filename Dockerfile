FROM debian:9.4
USER root
RUN mkdir /code
WORKDIR /code
ADD . /code/

RUN ./check_sudo.sh
RUN ./install_python.sh