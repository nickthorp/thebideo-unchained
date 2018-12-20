#!/usr/bin/env bash

# Stop and Remove and existing thebideo containers
docker stop thebideo
docker rm thebideo

# Remove any existing images
docker image rm thebideo:latest

# Build that container
docker build --rm -t thebideo:latest -f `pwd`/thebideo/docker/thebideo/Dockerfile .

echo $BUILD_NUMBER
# Run the container, should not be part of the build steps
# docker run -d -p 127.0.0.1:19000:9000 -p 127.0.0.1:19191:9191 --name thebideo -it thebideo:latest
# Run the DB migrate command, also should not be run during build time
# docker exec -it django python manage.py migrate