FROM ubuntu:20.04
LABEL maintainer "Charbel"
ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /ocr_api

RUN apt-get update && apt-get install -y --no-install-recommends \
        locales \
        python3-pip \
        pkg-config\
        curl \
        ffmpeg \
        libsm6 \
        libxext6
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
  dpkg-reconfigure --frontend=noninteractive locales && \
  update-locale LANG=en_US.UTF-8
ENV LANG en_US.UTF-8

RUN apt-get -y install tesseract-ocr

RUN pip3 install --upgrade pip
COPY docker/requirements.txt .
RUN pip3 install Pillow
RUN pip3 install python-multipart
RUN pip3 install -r requirements.txt





COPY . /ocr_api



EXPOSE 4200
CMD uvicorn main:app --host 0.0.0.0  --port 4200
