import pandas as pd
import glob
import sys

root_path = sys.argv[1]
output_file = sys.argv[2]

all_files = glob.glob(root_path + "\\results_*.csv")

all_rows = []

for filename in all_files:
    for chunk in  pd.read_csv(filename, chunksize=20000, index_col=None, header=0, low_memory=False):
        all_rows.append(chunk[['elapsed', 'success', 'allThreads']].copy())

frame = pd.concat(all_rows, axis=0, ignore_index=True)

frame.to_csv(root_path + '\\' + output_file,
                 encoding='utf-8', index=False)
