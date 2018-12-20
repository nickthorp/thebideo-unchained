#!/usr/bin/env bash

docker stop django

docker rm django

docker build -f ../thebideo/docker/thebideo/Dockerfile --force-rm -t thebideo:latest

docker run -d -p 19000:9000 -p 19191:9191 --name django