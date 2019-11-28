FROM python:3.6-slim

LABEL maintainer="imiguel10@correo.ugr.es"

COPY requirements.txt ./
COPY tasks.py ./
RUN pip install invoke
RUN invoke install

COPY src/ src/

EXPOSE 80

CMD ["invoke", "start"]
