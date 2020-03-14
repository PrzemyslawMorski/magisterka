docker build -t hello-world .
docker run --publish 6066:8080 --name hello-world-test --rm hello-world
