import pandas as pd
import glob
import sys

test = sys.argv[1]
system_name = sys.argv[1]

path = "D:\\Google Drive\\Magister\\Wyniki badan\\no-keep-alive\\%s\\%s" % (
    test, system_name)
all_files = glob.glob(path + "\\results_*.csv")

all_rows = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    all_rows.append(df)

frame = pd.concat(all_rows, axis=0, ignore_index=True)

projected = frame[['elapsed', 'success',
                   'bytes', 'sentBytes', 'allThreads']].copy()

projected.to_csv('output.csv', encoding='utf-8', index=False)
