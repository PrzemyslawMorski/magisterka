glances --export csv --export-csv-file usage_podman.csv -q &
podman run -p 9081:80 --name network_test --rm -d nginx