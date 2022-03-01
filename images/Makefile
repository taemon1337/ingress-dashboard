SHELL=/bin/bash
PWD=`pwd`
BASEIMAGE=`cat Dockerfile | head -n 1 | cut -d' ' -f2`
CACHE=~/.cache/pip
DOCKER_USER=`git config --get remote.origin.url | cut -d: -f2 | cut -d/ -f1`
PORT=8080
VERSION=`cat VERSION | head -n 1`
IMAGE=${DOCKER_USER}/image-api

shell:
	docker run --rm  -it -v ${PWD}:/app -v ${CACHE}:/root/.cache -w /app ${BASEIMAGE} /bin/sh

run:
	docker run --rm  -it -p ${PORT}:${PORT} -v ${PWD}:/app -v ${CACHE}:/root/.cache -w /app ${BASEIMAGE} /bin/sh run.sh

build:
	docker build -t ${IMAGE}:${VERSION} .

serve:
	docker run -it -e DEBUG=1 -p ${PORT}:${PORT} ${IMAGE}:${VERSION}

push:
	docker tag ${IMAGE}:${VERSION} ${IMAGE}:latest
	docker push ${IMAGE}:${VERSION}
	docker push ${IMAGE}:latest
