FROM python:3.8-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN apk add --no-cache git
RUN pip install -r requirements.txt

COPY . /app

RUN git clone git@github.com:cncf/artwork.git /app/artwork
ENV PORT=8080

ENTRYPOINT [ "python", "app.py" ]