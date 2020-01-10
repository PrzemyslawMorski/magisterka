FROM golang:latest 

RUN mkdir /app 
ADD . /app/ 
WORKDIR /app 

RUN go build -o hello-world . 

EXPOSE 80

CMD ["/app/hello-world"]