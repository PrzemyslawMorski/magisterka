docker run -d -p 9201:9200 docker.elastic.co/elasticsearch/elasticsearch:7.4.2

sleep 30s

curl -XPUT 'localhost:9201/companydatabase/_bulk' -H 'Content-Type: application/json' --data-binary @Employees100K.json