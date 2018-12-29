#!/usr/bin/env bash

# $BUILD_NUMBER is an environment variable intended to be in inherited from build automation (Jenkins)

# Remove any existing images
docker image rm nuggle/thebideo-unchained:latest

# Build that container
docker build --rm -t nuggle/thebideo-unchained:latest -t nuggle/thebideo-unchained:1.${BUILD_NUMBER} -f `pwd`/thebideo/docker/thebideo/Dockerfile .
