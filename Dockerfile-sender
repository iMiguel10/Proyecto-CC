FROM python:3.6-slim

LABEL maintainer="imiguel10@correo.ugr.es"

COPY requirements-sender.txt ./
COPY tasks.py ./

RUN pip install invoke
RUN invoke install --ms sender

COPY src/emailSender.py src/enviarEntradas.py src/

CMD ["invoke", "start", "--ms", "sender"]
