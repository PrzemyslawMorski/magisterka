import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from numpy import genfromtxt
import glob
import sys
import os

root_path = sys.argv[1]
test_name = sys.argv[2]
system_name = sys.argv[3]
column = sys.argv[4]

all_files = glob.glob(root_path + "\\*_step.csv")

test_results_raw = []

for filename in all_files:
    df = pd.read_csv(filename, sep=',', header=0, low_memory=False)

    column_values = df[column].values
    num_rows = df.shape[0]

    k2, p1 = stats.normaltest(column_values)
    sh, p2 = stats.shapiro(column_values)

    this_test_result = {
        'test': test_name,
        'system': system_name,
        'step_name': os.path.basename(filename),
        'num rows': num_rows,
        'dagostino&pearson stat': k2,
        'dagostino&pearson p-value': p1,
        'shapiro&wilk stat': sh,
        'shapiro&wilk p-value': p2
    }

    test_results_raw.append(this_test_result)


test_results = pd.DataFrame(data=test_results_raw)
test_results.to_csv('%s\\%s' % (root_path, column + '_normality.csv'),
                    encoding='utf-8', index=False)
