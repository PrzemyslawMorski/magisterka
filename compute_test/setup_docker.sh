glances --export csv --export-csv-file usage_docker.csv -q &
docker run -p 8081:8080 --rm --name compute_test pmorski/compute_test_fibonacci