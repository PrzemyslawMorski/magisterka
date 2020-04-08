singularity build --sandbox --fix-perms network_test_sandbox/ docker://nginx
sudo singularity run --writable network_test_sandbox &