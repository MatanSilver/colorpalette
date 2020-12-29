FROM alpine:3.3

# Install app dependencies

ENV LIBRARY_PATH=/lib:/usr/lib
RUN apk update
RUN apk add --no-cache python3
RUN apk add --no-cache python3-dev
RUN apk add --no-cache zlib-dev
RUN apk add --no-cache jpeg-dev
RUN apk add --no-cache build-base
RUN apk add --no-cache git


RUN python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools wheel

# RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

RUN mkdir -p /usr/src/app; exit 0
WORKDIR /usr/src/app
COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8080
CMD [ "python3", "manage.py", "runserver" ]
