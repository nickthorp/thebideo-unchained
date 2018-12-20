docker stop django

docker rm django
docker image rm thebideo:latest
docker build --rm -t thebideo:latest -f ../thebideo/docker/thebideo/Dockerfile ../

docker run -d -p 127.0.0.1:19000:9000 -p 127.0.0.1:19191:9191 --name django -it thebideo

docker exec -it django python manage.py migrate