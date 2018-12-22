#!/usr/bin/env bash

# $BUILD_NUMBER is an environment variable intended to be in inherited from build automation (Jenkins)

# Remove any existing images
docker image rm thebideo:latest

# Build that container
docker build --rm -t thebideo:latest -t thebideo:1.${BUILD_NUMBER} -f `pwd`/thebideo/docker/thebideo/Dockerfile .
