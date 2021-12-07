FROM ubuntu:20.04
LABEL maintainer "Charbel"
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
        locales \
        python3-pip \
        pkg-config\
        curl
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
  dpkg-reconfigure --frontend=noninteractive locales && \
  update-locale LANG=en_US.UTF-8
ENV LANG en_US.UTF-8

RUN apt-get -y install tesseract-ocr

RUN pip3 install --upgrade pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt





COPY ./ /ocr_api

WORKDIR /ocr_api


CMD uvicorn main:app --host 0.0.0.0  --port 4222
