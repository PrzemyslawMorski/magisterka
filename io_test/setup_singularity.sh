sudo echo "vm.max_map_count=262144" >> /etc/sysctl.conf

singularity build --fix-perms --sandbox io_test_sandbox/ docker://docker.elastic.co/elasticsearch/elasticsearch:7.4.2
singularity run --writable io_test_sandbox &

sleep 30s

curl -XPUT 'localhost:9200/companydatabase/_bulk' -H 'Content-Type: application/json' --data-binary @Employees100K.json