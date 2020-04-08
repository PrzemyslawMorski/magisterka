FROM golang:latest
LABEL Przemysław Morski <morski.przemek@gmail.com>
RUN mkdir /app
ADD . /app/
WORKDIR /app
RUN go build -o main .
EXPOSE 8080
CMD ["/app/main"]