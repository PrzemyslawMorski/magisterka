import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from numpy import genfromtxt
import glob
import sys
import os

column = sys.argv[1]
test_type = sys.argv[2]
results_folder = sys.argv[3]
step_file_suffix = sys.argv[4]

# column = 'elapsed'
# test_type = 'network'
# results_folder = 'results_steps'
# step_file_suffix = '_step.csv'

base_path = r'D:\Google Drive\Magister\Wyniki badan\no-keep-alive\%s' % (
    test_type)
path_to_format = base_path + r'\%s\%s\%s%s'

results = []

for i in range(1, 11):
    df_docker = pd.read_csv(path_to_format % ('docker', results_folder, str(
        i), step_file_suffix), sep=',', header=0, low_memory=False)
    df_podman = pd.read_csv(path_to_format % ('podman', results_folder, str(
        i), step_file_suffix), sep=',', header=0, low_memory=False)
    df_singularity = pd.read_csv(path_to_format % ('singularity', results_folder, str(
        i), step_file_suffix), sep=',', header=0, low_memory=False)

    docker_description = df_docker[column].describe()
    podman_description = df_podman[column].describe()
    singularity_description = df_singularity[column].describe()

    docker_mean = docker_description['mean']
    docker_diff_percentile = docker_description['75%'] - docker_description['25%']

    podman_mean = podman_description['mean']
    podman_diff_percentile = podman_description['75%'] - podman_description['25%']

    singularity_mean = singularity_description['mean']
    singularity_diff_percentile = singularity_description['75%'] - singularity_description['25%']

    results.append({
        'Krok wzostu liczby uzytkownikow': i,
        'Metryka': column,
        'Mediana docker': docker_mean,
        'Rozstep miedzykwantylowy docker': docker_diff_percentile,
        'Mediana podman': podman_mean,
        'Rozstep miedzykwantylowy podman': podman_diff_percentile,
        'Mediana singularity': singularity_mean,
        'Rozstep miedzykwantylowy singularity': singularity_diff_percentile,
    })

test_results = pd.DataFrame(data=results)
test_results.to_csv('%s\\%s' % (base_path, column + '_describe.csv'),
                    encoding='utf-8', index=False)
