singularity build --sandbox --fix-perms compute_test_sandbox/ docker://pmorski/compute_test_fibonacci
singularity run --writeable compute_test_sandbox &