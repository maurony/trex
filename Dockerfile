FROM ubuntu:18.04

ENV TESSDATA_PREFIX=/usr/share/tesseract-ocr/4.00/tessdata

RUN sed -Ei 's/^# deb-src /deb-src /' /etc/apt/sources.list \
    && apt-get update \
    && apt-get install \
    build-essential \
    cmake \
    unzip \
    pkg-config\ 
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    libv4l-dev \
    libxvidcore-dev \
    libx264-dev \
    libatlas-base-dev \
    gfortran \
    tesseract-ocr -y \
    tesseract-ocr-deu -y \
    tesseract-ocr-fra -y \
    python3 \
    python-setuptools \
    python3-pip \
    wget \
    unzip \
    && apt-get -y install poppler-utils \
    && apt-get clean \
    && apt-get autoremove 

WORKDIR /home/coding

#RUN wget -O opencv.zip https://github.com/opencv/opencv/archive/4.1.0.zip \
#    && wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.1.0.zip \
#    && unzip opencv.zip \
#    && unzip opencv_contrib.zip \ 
#    && mv opencv-4.1.0 opencv \
#    && mv opencv_contrib-4.1.0 opencv_contrib
    

RUN pip3 install pillow pytesseract imutils pdf2image opencv-python-headless opencv-contrib-python-headless


