FROM python:3.6-slim

LABEL maintainer="imiguel10@correo.ugr.es"

COPY requirements.txt ./
COPY tasks.py ./
RUN pip install invoke
RUN invoke install

COPY src/ src/

ARG MAIL
ARG MAIL_PASS
ARG BD

ENV MAIL ${MAIL}
ENV MAIL_PASS ${MAIL_PASS}
ENV BD ${BD}

EXPOSE 80

CMD ["gunicorn","-b","0.0.0.0:80","app:app"]
