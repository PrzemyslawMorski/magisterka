docker run --publish 8080:80 --name compute_test -d pmorski/compute_test_fibonacci
docker run --publish 8070:80 --name io_test -d pmorski/io_test_bold_db
docker run --publish 8060:80 --name network_test -d pmorski/network_test_hello-world

singularity run --network-args "portmap=9080:80/tcp" compute_test.sif
singularity run --network-args "portmap=9070:80/tcp" io_test.sif
singularity run --network-args "portmap=9060:80/tcp" network_test.sif
