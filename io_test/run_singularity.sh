# sudo echo "vm.max_map_count=262144" >> /etc/sysctl.conf

export ES_JAVA_OPTS="-Xms6g -Xmx6g"

sudo singularity instance start \
    --bind ./magisterka/io_test/elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml \
    --writable-tmpfs \
    docker://docker.elastic.co/elasticsearch/elasticsearch:7.6.2 \
    io_test

sudo singularity run --security uid:1000 instance://io_test &

sleep 40