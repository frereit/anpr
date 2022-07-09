# i chose ubuntu as base, because the binaries were build on Ubuntu 18
FROM ubuntu:18.04

# ualpr
RUN apt update && apt install git -y

RUN git clone https://github.com/DoubangoTelecom/ultimateALPR-SDK /app/ultimateALPR-SDK

WORKDIR /app/ultimateALPR-SDK/binaries/linux/x86_64/
RUN chmod +x recognizer

ADD https://doubango.org/deep_learning/libtensorflow_r1.14_cpu_linux_x86-64.tar.gz /app/ultimateALPR-SDK/binaries/linux/x86_64/
RUN tar -xvf libtensorflow_r1.14_cpu_linux_x86-64.tar.gz

# install ffmpeg
RUN apt install ffmpeg -y

# script
COPY ./generate-boundingboxes.sh /app/script/generate-bounding-boxes.sh
RUN chmod +x /app/script/generate-bounding-boxes.sh

RUN mkdir /app/tmp
RUN mkdir /app/output

CMD /app/script/generate-bounding-boxes.sh