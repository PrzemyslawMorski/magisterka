import pandas as pd
import glob

merged_file = "output.csv"

data = pd.read_csv(merged_file, index_col=None, header=0)

step = data['allThreads'].max() / 10

for i in range(1, 11):
    step_rows = data.loc[
        (data['allThreads'] <= i * step)]
    step_rows = step_rows.loc[
        (step_rows['allThreads'] > (i-1) * step)]
    step_rows.to_csv(str(i) + '_step.csv', encoding='utf-8', index=False)
