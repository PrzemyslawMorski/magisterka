# sudo echo "vm.max_map_count=262144" >> /etc/sysctl.conf

export ES_JAVA_OPTS="-Xms6g -Xmx6g"

bash -c "singularity build --fix-perms --sandbox io_test_sandbox/ docker://docker.elastic.co/elasticsearch/elasticsearch:7.4.2"
bash -c "cp ./magisterka/io_test/elasticsearch.yml ./io_test_sandbox/usr/share/elasticsearch/config"

bash -c "ingularity run --fakeroot --writable io_test_sandbox &"
