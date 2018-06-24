FROM debian:9.4
USER root
RUN mkdir /authorizeKerberos
WORKDIR /authorizeKerberos
ADD . /authorizeKerberos/

RUN ./check_sudo.sh
RUN ./install_python.sh