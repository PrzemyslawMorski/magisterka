import pandas as pd
import glob
import sys


root_path = sys.argv[1]
test = sys.argv[2]
system_name = sys.argv[3]

base_path = "%s\\%s\\%s" % (root_path, test, system_name)
all_files = glob.glob(base_path + "\\usage_*.csv")

all_rows = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    all_rows.append(df)

frame = pd.concat(all_rows, axis=0, ignore_index=True)

projected = frame[['elapsed', 'success',
                   'bytes', 'sentBytes', 'allThreads']].copy()

projected.to_csv(base_path + '\\results_merged.csv',
                 encoding='utf-8', index=False)
