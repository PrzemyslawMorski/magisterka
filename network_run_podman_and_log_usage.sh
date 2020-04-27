glances_id=$(glances --export csv --export-csv-file usage_podman.csv -q &)
podman_id=$(podman run -p 9081:80 --name network_test --rm -d nginx)

read -p "Kill the container? " answer

podman kill $podman_id
podman container rm $podman_id
kill $glances_id