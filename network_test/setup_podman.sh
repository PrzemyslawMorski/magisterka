glances --export csv --export-csv-file usage_podman.csv -q &
podman run -p 9080:80 --name network_test --rm nginx