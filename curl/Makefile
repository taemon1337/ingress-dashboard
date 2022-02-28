SHELL=/bin/bash
DOCKER_USER=`git config --get remote.origin.url | cut -d: -f2 | cut -d/ -f1`
IMAGE=${DOCKER_USER}/k8s-curl
VERSION=`cat ./VERSION | head -n 1`

.PHONY: build
build:
	docker build -t ${IMAGE}:${VERSION} .

push:
	docker push ${IMAGE}:${VERSION}