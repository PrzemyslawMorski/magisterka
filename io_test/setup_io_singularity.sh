singularity build io_test.sif docker://docker.elastic.co/elasticsearch/elasticsearch:7.4.2

singularity run --network-args "portmap=9202:9200/tcp" io_test.sif &

sleep 30s

curl -XPUT 'localhost:9202/companydatabase/_bulk' -H 'Content-Type: application/json' --data-binary @Employees100K.json