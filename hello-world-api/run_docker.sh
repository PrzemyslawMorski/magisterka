docker build -t golang-hello-world -f Dockerfile .
docker run -it -p 8095:80 golang-hello-world
curl http://localhost:8095/asda