import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from numpy import genfromtxt
import glob
import sys
import os

column =  sys.argv[1]
test_type = sys.argv[2]
results_folder = sys.argv[3]
step_file_suffix = sys.argv[4]

system_1 = sys.argv[5]
system_2 = sys.argv[6]

# column = 'elapsed'
# test_type = 'network'
# results_folder = 'results_steps'
# step_file_suffix = '_step.csv'

# system_1 = 'docker'
# system_2 = 'podman'

base_path = r'D:\Google Drive\Magister\Wyniki badan\no-keep-alive\%s' % (test_type) 
path_to_format = base_path + r'\%s\%s\%s%s'
# path_to_format = base_path + r'\%s\%s\%s_usage_step.csv'

results = []

for i in range(1, 11):
    df_docker = pd.read_csv(path_to_format % (system_1, results_folder, str(i), step_file_suffix), sep=',', header=0, low_memory=False)
    df_podman = pd.read_csv(path_to_format % (system_2, results_folder, str(i), step_file_suffix), sep=',', header=0, low_memory=False)
    
    k2, p1 = stats.mannwhitneyu(df_docker[column], df_podman[column])

    results.append({'Krok wzostu liczby uzytkownikow': i, 'metryka': column, 'Statystyka Mann-Whitney U': k2, 'P-value Mann-Whitney U': p1})

test_results = pd.DataFrame(data=results)
test_results.to_csv('%s\\%s_%s_%s_mannwhitneyu.csv' % (base_path, column, system_1, system_2),
                    encoding='utf-8', index=False)