FROM ubuntu:latest

LABEL maintainer="imiguel10@correo.ugr.es"

RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN ln -s /usr/bin/pip3 /usr/bin/pip
COPY requirements.txt ./
COPY tasks.py ./
RUN pip install invoke
RUN invoke install

COPY src/ src/

EXPOSE 8080

CMD ["invoke", "start"]
