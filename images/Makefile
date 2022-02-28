SHELL=/bin/bash
PWD=`pwd`
BASEIMAGE=`cat Dockerfile | head -n 1 | cut -d' ' -f2`
CACHE=~/.cache/pip
PORT=8080
IMAGE=image-api
VERSION=`cat VERSION | head -n 1`
DOCKER_USER=`git config --get remote.origin.url | cut -d: -f2 | cut -d/ -f1`

shell:
	docker run --rm  -it -v ${PWD}:/app -v ${CACHE}:/root/.cache -w /app ${BASEIMAGE} /bin/sh

run:
	docker run --rm  -it -p ${PORT}:${PORT} -v ${PWD}:/app -v ${CACHE}:/root/.cache -w /app ${BASEIMAGE} /bin/sh run.sh

build:
	docker build -t ${IMAGE}:${VERSION} .

serve:
	docker run -it -e DEBUG=1 -p ${PORT}:${PORT} ${IMAGE}:${VERSION}

release:
	docker tag ${IMAGE}:${VERSION} ${DOCKER_USER}/${IMAGE}:${VERSION}
	docker tag ${DOCKER_USER}/${IMAGE}:${VERSION} ${DOCKER_USER}/${IMAGE}:latest
	docker push ${DOCKER_USER}/${IMAGE}:${VERSION}
	docker push ${DOCKER_USER}/${IMAGE}:latest
