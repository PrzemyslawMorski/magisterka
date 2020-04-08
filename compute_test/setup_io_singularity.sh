singularity build compute_test.sif docker://pmorski/compute_test_fibonacci
singularity run --network-args "portmap=8002:8080/tcp" compute_test.sif &