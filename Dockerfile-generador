FROM python:3.6-slim

LABEL maintainer="imiguel10@correo.ugr.es"

COPY requirements-generador.txt ./
COPY tasks.py ./

RUN pip install invoke
RUN invoke install --ms generador

COPY src/generadorEntradas.py src/generadorentradasPDF.py src/

CMD ["invoke", "start", "--ms", "generador"]
