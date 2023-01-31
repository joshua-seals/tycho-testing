SHELL 			 := /bin/bash
BRANCH_NAME	 	 := $(shell git branch --show-current | sed -r 's/[/]+/_/g')
override VERSION := ${BRANCH_NAME}-${VER}
PYTHON       := python3
DOCKER_REPO  = docker.io
DOCKER_OWNER = helxplatform
DOCKER_APP	 = tycho-api
DOCKER_TAG   = ${VERSION}
DOCKER_IMAGE = ${DOCKER_OWNER}/${DOCKER_APP}:$(DOCKER_TAG)

.DEFAULT_GOAL = help

.PHONY: help init clean install test build image publish

version:
	${PYTHON} --version
	echo ${VERSION}

#help: List available tasks on this project
help:
	@grep -E '^#[a-zA-Z\.\-]+:.*$$' $(MAKEFILE_LIST) | tr -d '#' | awk 'BEGIN {FS = ": "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

#init: Initialize the repository with things like git commit hooks
init:
	git --version
	@echo "Please make sure your git version is greater than 2.9.0. If it's not, this command will fail."
	git config --local core.hooksPath .githooks/

clean:
	${PYTHON} -m pip uninstall -y tycho-api
	${PYTHON} -m pip uninstall -y -r requirements.txt

install:
	${PYTHON} -m pip install --upgrade pip
	${PYTHON} -m pip install --upgrade wheel
	${PYTHON} -m pip install --upgrade setuptools
	${PYTHON} -m pip install -r requirements.txt
	${PYTHON} -m pip install .

#test: Run all tests
test:
	# ${PYTHON} -m flake8 src
	${PYTHON} -m pytest tests

package.build: ${PYTHON} -m build

package.release:
	${PYTHON} -m twine upload dist/*
	rm -rf dist

build:
	@if [ -z "$(VER)" ]; then echo "Please provide a value for the VER variable like this:"; echo "make VER=4 <target>"; false; fi;
	docker build -t ${DOCKER_IMAGE} -f Dockerfile .

publish: build
	@if [ -z "$(VER)" ]; then echo "Please provide a value for the VER variable like this:"; echo "make VER=4 <target>"; echo "Here are the images you have already built that can be published:" ; docker images | grep "IMAGE ID"; docker images | grep "${DOCKER_OWNER}/${DOCKER_APP}"; false; fi;
	docker tag ${DOCKER_IMAGE} ${DOCKER_REPO}/${DOCKER_IMAGE}
	docker push ${DOCKER_REPO}/${DOCKER_IMAGE}
