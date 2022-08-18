FROM python:3.6-alpine

RUN apk update
RUN apk --no-cache add wget \
        #  python \
         nginx \
         ca-certificates

# RUN apt-get -y update && apt-get install -y --no-install-recommends \
#          wget \
#          python \
#          nginx \
#          ca-certificates \
#     && rm -rf /var/lib/apt/lists/*


RUN wget https://bootstrap.pypa.io/pip/3.6/get-pip.py && python get-pip.py && \
    pip3 install flask gevent gunicorn dill
      
        
ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"

# Copy the directory 'script' which contains our script file to the /opt/program directory of the image.
COPY Files /opt/program
RUN mkdir -p /opt/ml/model
COPY Model/hello-world-model.pkl /opt/ml/model
WORKDIR /opt/program
