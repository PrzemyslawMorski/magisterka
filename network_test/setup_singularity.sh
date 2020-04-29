singularity build --sandbox --fix-perms network_test_sandbox/ docker://nginx

glances --export csv --export-csv-file usage_singularity.csv -q &

sudo singularity run --writable network_test_sandbox &