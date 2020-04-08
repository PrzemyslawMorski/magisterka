docker run -p 8001:8080 --name compute_test -d pmorski/compute_test_fibonacci
singularity run --network-args "portmap=8002:8080/tcp" compute_test.sif

docker run -p 9201:9200 --name io_test -d pmorski/io_test_bold_db
singularity run --network-args "portmap=9202:9200/tcp" io_test.sif

docker run -p 8501:80 --name network_test --rm -d nginx
singularity run --network-args "portmap=8502:80/tcp" network_test.sif


