FROM python:3.9-slim-bullseye

ARG VERSION=7.3.3

RUN apt-get update 
RUN apt install -y git build-essential pkg-config gettext libffi-dev
RUN git clone https://github.com/adafruit/circuitpython.git
WORKDIR /circuitpython/
RUN git checkout $VERSION
RUN make fetch-submodules
RUN pip3 install -r requirements-dev.txt
RUN make -C mpy-cross
WORKDIR /circuitpython/ports/unix/
RUN make axtls
RUN make micropython
RUN make install
WORKDIR /
RUN rm -rf /circuitpython
RUN apt purge --auto-remove -y git build-essential pkg-config gettext libffi-dev
CMD ["/usr/local/bin/micropython"]