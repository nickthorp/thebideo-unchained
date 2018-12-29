#!/usr/bin/env bash

# $BUILD_NUMBER is an environment variable intended to be in inherited from build automation (Jenkins)
PORTS="-p 127.0.0.1:9000:9000 -p 127.0.0.1:9191:9191"
VOLUMES="-v /etc/thebideo:/etc/thebideo"
DOCKER_ENV="--env ENV=PRODUCTION"

# Stop and Remove and existing thebideo containers
docker stop nuggle/thebideo-unchained
docker rm nuggle/thebideo-unchained

# Run the container, should not be part of the build steps
docker run -d ${PORTS} ${VOLUMES} ${DOCKER_ENV} --name nuggle/thebideo-unchained -it nuggle/thebideo-unchained:1.$BUILD_NUMBER
# Run the DB migrate command, also should not be run during build time
sleep 10 # gotta give it some time to warm up
docker exec -i nuggle/thebideo-unchained python manage.py migrate