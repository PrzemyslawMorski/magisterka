podman run -d --name io_test --rm -e discovery.type=single-node -e "ES_JAVA_OPTS=-Xms6g -Xmx6g" -v $(pwd)/magisterka/io_test/elasticsearch.yml:/usr/share/elasticsearch/config/elasicsearch.yml -p 9200:9200 docker.elastic.co/elasticsearch/elasticsearch:7.4.2

sleep 30s

curl -XPUT 'localhost:9200/companydatabase/_bulk' -H 'Content-Type: application/json' --data-binary @./magisterka/io_test/Employees100K.json