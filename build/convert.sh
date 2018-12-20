#!/usr/bin/env bash

# Stop running/existing container
docker stop sass-converter
docker rm sass-converter
# Build sass-converter if necessary
docker build --rm -t sass:latest -f `pwd`/thebideo/docker/sass/Dockerfile .
# Run that shit!
docker run -d -v `pwd`/thebideo/_sass/:/src -v `pwd`/thebideo/bideosite/static/bideosite/:/dest --name sass-converter -it sass:latest
