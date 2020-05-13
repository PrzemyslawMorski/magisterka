curl -XPUT 'localhost:9200/companydatabase/_bulk' -H 'Content-Type: application/json' --data-binary @./magisterka/io_test/Employees100K.json
curl -XPUT "localhost:9200/companydatabase/_settings" -H 'Content-Type: application/json' -d'{"index.requests.cache.enable":true}'

