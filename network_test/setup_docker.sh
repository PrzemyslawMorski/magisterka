glances --export csv --export-csv-file usage_docker.csv -q &
docker run -p 9080:80 --name network_test --rm nginx