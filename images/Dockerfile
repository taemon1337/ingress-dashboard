FROM python:3.8-alpine

RUN apk add --no-cache git
RUN git clone --depth 1 --single-branch --branch master https://github.com/cncf/artwork.git

FROM python:3.8-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN apk add --no-cache git
RUN pip install -r requirements.txt

COPY . /app
COPY --from=0 /artwork /app/artwork

ENV PORT=8080

ENTRYPOINT [ "gunicorn", "-w", "4", "app:app" ]