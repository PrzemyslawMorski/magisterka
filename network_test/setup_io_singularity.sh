singularity build network_test.sif docker://nginx

singularity run --network-args "portmap=8502:80/tcp" network_test.sif &
