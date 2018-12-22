#!/usr/bin/env bash

# $BUILD_NUMBER is an environment variable intended to be in inherited from build automation (Jenkins)

# Run the container, should not be part of the build steps
docker run -d -p 127.0.0.1:19000:9000 -p 127.0.0.1:19191:9191 --name thebideo -it thebideo:1.$BUILD_NUMBER
# Run the DB migrate command, also should not be run during build time
docker exec -it thebideo python manage.py migrate