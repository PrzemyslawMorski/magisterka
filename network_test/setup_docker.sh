glances_id=$(glances --export csv --export-csv-file usage_docker.csv -q &)
docker_id=$(docker run -p 9080:80 --name network_test --rm -d nginx)

read -p "Kill the container? " answer

docker kill $docker_id
docker container rm $docker_id
kill $glances_id