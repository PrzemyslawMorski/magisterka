import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from numpy import genfromtxt
import glob
import sys
import os

test_type = sys.argv[1]
# test_type = 'compute'

base_path = r'D:\Google Drive\Magister\Wyniki badan\no-keep-alive\%s' % (
    test_type)
path_to_format = base_path + r'\%s\results_steps\%s_step.csv'

results = []

for i in range(1, 11):
    df_docker = pd.read_csv(path_to_format % (
        'docker', str(i)), sep=',', header=0, low_memory=False)
    df_podman = pd.read_csv(path_to_format % (
        'podman', str(i)), sep=',', header=0, low_memory=False)
    df_singularity = pd.read_csv(path_to_format % (
        'singularity', str(i)), sep=',', header=0, low_memory=False)

    docker_count = df_docker.shape[0]
    docker_num_successes = len(df_docker[df_docker['success'] == True].index)
    docker_num_fails = docker_count - docker_num_successes
    docker_error_rate = docker_num_fails/docker_count

    podman_count = df_podman.shape[0]
    podman_num_successes = len(df_podman[df_podman['success'] == True].index)
    podman_num_fails = podman_count - podman_num_successes
    podman_error_rate = podman_num_fails/podman_count

    singularity_count = df_singularity.shape[0]
    singularity_num_successes = len(df_singularity[df_singularity['success'] == True].index)
    singularity_num_fails = singularity_count - singularity_num_successes
    singularity_error_rate = singularity_num_fails/singularity_count

    results.append({
        'Krok wzostu liczby uzytkownikow': i,
        'Liczba obsluzonych zapytan docker': docker_count,
        'Liczba obsluzonych zapytan  podman': podman_count,
        'Liczba obsluzonych zapytan  singularity': singularity_count,
        'Liczba blednie obsluzonych zapytan docker': docker_num_fails,
        'Liczba blednie obsluzonych zapytan  podman': podman_num_fails,
        'Liczba blednie obsluzonych zapytan  singularity': singularity_num_fails,
        'Wspolczynnik bledu docker': docker_error_rate,
        'Wspolczynnik bledu podman': podman_error_rate,
        'Wspolczynnik bledu singularity': singularity_error_rate
    })

test_results = pd.DataFrame(data=results)
test_results.to_csv('%s\\%s' % (base_path, 'error_rate_describe.csv'),
                    encoding='utf-8', index=False)
