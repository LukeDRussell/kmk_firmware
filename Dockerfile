FROM python:3.9-slim-bullseye as build

ARG VERSION=7.3.3

RUN apt-get update 
RUN apt install -y git build-essential pkg-config gettext libffi-dev --no-install-recommends
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
CMD ["/usr/local/bin/micropython"]

FROM alpine:latest as main
COPY --from=build /usr/local/bin/micropython /usr/local/bin/micropython
CMD ["/usr/local/bin/micropython"]