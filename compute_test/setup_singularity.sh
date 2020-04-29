singularity build --sandbox --fix-perms compute_test_sandbox/ docker://pmorski/compute_test_fibonacci

glances --export csv --export-csv-file usage_singularity.csv -q &

singularity run --writable compute_test_sandbox &