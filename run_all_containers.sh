cd compute_test
bash build_push_docker_hub.sh
bash setup_docker.sh
bash setup_singularity.sh
cd ..

cd io_test
bash setup_docker.sh
bash setup_singularity.sh
cd ..

cd network_test
bash setup_docker.sh
bash setup_singularity.sh
cd ..
