singularity build --sandbox --fix-perms network_test_sandbox/ docker://nginx

sudo singularity instance start --writable network_test_sandbox &