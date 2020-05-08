sudo singularity instance start --writable-tmpfs docker://nginx network_test
sudo singularity exec instance://network_test nginx