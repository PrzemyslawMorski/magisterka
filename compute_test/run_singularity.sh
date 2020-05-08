sudo singularity instance start --writable-tmpfs docker://pmorski/compute_test_fibonacci compute_test
sudo singularity exec instance://compute_test /app/main &
