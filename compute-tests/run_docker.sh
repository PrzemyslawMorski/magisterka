docker build -t fibonacci .
docker run --publish 6060:8080 --name fibonacci-test --rm fibonacci
