SHELL=/bin/bash
DOCKER_USER=`git config --get remote.origin.url | cut -d: -f2 | cut -d/ -f1`
IMAGE="${DOCKER_USER}/ingress-dashboard"
VERSION=`cat package.json | grep version | cut -d: -f2 | tr -d '" ,'`

.PHONY: build
build:
	docker build -t ${IMAGE}:${VERSION} .

push:
	docker push ${IMAGE}:${VERSION}