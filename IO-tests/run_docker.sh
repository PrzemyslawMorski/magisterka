docker build -t bolt-db .
docker run --publish 6069:8080 --name bolt-db-test --rm bolt-db
