FROM python:3.6-alpine

RUN apk update && \
    apk upgrade

RUN apk --no-cache add wget \
         nginx \
         ca-certificates

RUN wget https://bootstrap.pypa.io/pip/3.6/get-pip.py && python get-pip.py && \
    pip3 install flask gevent gunicorn dill
      
ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"

COPY Files /opt/program
RUN mkdir -p /opt/ml/model
COPY Model/hello-world-model.pkl /opt/ml/model
WORKDIR /opt/program
