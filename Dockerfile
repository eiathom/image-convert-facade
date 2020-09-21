FROM python:3.6-slim

# essential packages to allow fetching, installation and use of magick program

RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    make

# installing the magick program

WORKDIR /opt
RUN wget http://www.imagemagick.org/download/ImageMagick-7.0.10-29.tar.gz
RUN tar xvzf ImageMagick-7.0.10-29.tar.gz
WORKDIR /opt/ImageMagick-7.0.10-29
RUN ./configure
RUN make
RUN make install
RUN ldconfig /usr/local/lib
RUN magick -version

# installing 'this' library

ARG INSTALL_LOCATION=/usr/local/share
ARG INSTALL_DIRECTORY=/code
ARG INSTALL_PATH=${INSTALL_LOCATION}${INSTALL_DIRECTORY}

RUN mkdir ${INSTALL_PATH}

WORKDIR ${INSTALL_PATH}

COPY . ${INSTALL_PATH}

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH ${INSTALL_PATH}

RUN make install

# Docker will attempt to execute this directly (without an interperter)
# variables and variable expansion thus are not recognised
# running with an interperter - sh in this instance - solves this to a degree 
CMD ["sh", "-c", "$(find . -name bootstrap.sh)"]
