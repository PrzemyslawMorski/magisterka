glances --export csv --export-csv-file usage_docker.csv -q &

docker run -d --rm -e discovery.type=single-node -e "ES_JAVA_OPTS=-Xms6g -Xmx6g" -v $(pwd)/elasticsearch.yml:/usr/share/elasticsearch/config/elasicsearch.yml -p 9201:9200 docker.elastic.co/elasticsearch/elasticsearch:7.4.2

sleep 30s

curl -XPUT 'localhost:9201/companydatabase/_bulk' -H 'Content-Type: application/json' --data-binary @Employees100K.json