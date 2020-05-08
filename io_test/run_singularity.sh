# sudo echo "vm.max_map_count=262144" >> /etc/sysctl.conf

export ES_JAVA_OPTS="-Xms6g -Xmx6g"

singularity build --fix-perms --sandbox io_test_sandbox/ docker://docker.elastic.co/elasticsearch/elasticsearch:7.4.2
cp ./magisterka/io_test/elasticsearch.yml ./io_test_sandbox/usr/share/elasticsearch/config

singularity run --fakeroot --writable io_test_sandbox &

sleep 30s

curl -XPUT 'localhost:9200/companydatabase/_bulk' -H 'Content-Type: application/json' --data-binary @./magisterka/io_test/Employees100K.json
