glances --export csv --export-csv-file usage_podman.csv -q &

podman run -d --rm -e discovery.type=single-node -v $(pwd)/elasticsearch.yml:/usr/share/elasticsearch/config/elasicsearch.yml -p 9200:9200 docker.elastic.co/elasticsearch/elasticsearch:7.4.2

sleep 30s

curl -XPUT 'localhost:9200/companydatabase/_bulk' -H 'Content-Type: application/json' --data-binary @Employees100K.json