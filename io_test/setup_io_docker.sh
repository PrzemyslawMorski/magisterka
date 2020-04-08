docker run -d -p 9201:9200 pmorski/io_test_elasticsearch

sleep 30s

curl -XPUT 'localhost:9201/companydatabase/_bulk' --data-binary @Employees100K.json