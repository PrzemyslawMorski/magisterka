singularity build --fix-perms --sandbox io_test_sandbox/ docker://pmorski/io_test_elasticsearch
singularity run --writable io_test_sandbox &

sleep 30s

curl -XPUT 'localhost:9202/companydatabase/_bulk' -H 'Content-Type: application/json' --data-binary @Employees100K.json