FROM alpine:3.3

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies

RUN apk add --no-cache python
RUN apk add --no-cache py-pip
RUN apk add --no-cache git
RUN git clone https://github.com/MatanSilver/colorpalette.git .
RUN apk add --no-cache build-base python-dev jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h
RUN pip install -r requirements.txt

EXPOSE 8080
CMD [ "python", "manage.py", "runserver" ]
