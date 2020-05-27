import pandas as pd
import glob
import sys
import math
from pathlib import Path

root_path = sys.argv[1]
output_file = sys.argv[2]

Path(root_path + "\\usage_steps").mkdir(parents=True, exist_ok=True)


all_files = glob.glob(root_path + "\\usage_*.csv")

all_rows = []

for filename in all_files:
    for chunk in  pd.read_csv(filename, chunksize=20000, index_col=None, header=0, low_memory=False):
        important_columns = chunk[['now', 'cpu.total', 'mem.percent']].copy()
        important_columns['now'] = pd.to_datetime(important_columns['now'])
        
        min_date = important_columns['now'].min()
        important_columns['now'] = important_columns['now'].apply(lambda x: math.floor((x - min_date).total_seconds()))

        all_rows.append(important_columns)

frame = pd.concat(all_rows, axis=0, ignore_index=True)

frame.to_csv(root_path + '\\usage_steps\\' + output_file,
                 encoding='utf-8', index=False)
