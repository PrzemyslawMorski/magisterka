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

# column = 'mem.percent'
# test_type = 'io index'
# results_folder = 'usage_steps'

base_path = r'D:\Google Drive\Magister\Wyniki badan\no-keep-alive\%s' % (test_type) 
path_to_format = base_path + r'\%s\%s\%s%s'

results = []

for i in range(1, 11):
    df_docker = pd.read_csv(path_to_format % ('docker', results_folder, str(i), step_file_suffix), sep=',', header=0, low_memory=False)
    df_podman = pd.read_csv(path_to_format % ('podman', results_folder, str(i), step_file_suffix), sep=',', header=0, low_memory=False)
    df_singularity = pd.read_csv(path_to_format % ('singularity', results_folder, str(i), step_file_suffix), sep=',', header=0, low_memory=False)
    
    k2, p1 = stats.kruskal(df_docker[column], df_podman[column], df_singularity[column])

    results.append({'Krok wzostu liczby uzytkownikow': i, 'metryka': column, 'Statystyka Kruskal': k2, 'P-value Kruskal': p1})

test_results = pd.DataFrame(data=results)
test_results.to_csv('%s\\%s' % (base_path, column + '_kruskal.csv'),
                    encoding='utf-8', index=False)