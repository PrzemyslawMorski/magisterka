import pandas as pd
import glob
import sys

root_path = sys.argv[1]
merged_file = sys.argv[2]

data = pd.read_csv('%s\\%s' % (root_path, merged_file),
                   index_col=None, header=0)

step = data['now'].max() / 10

for i in range(1, 11):
    step_rows = data.loc[
        (data['now'] <= i * step)]
    step_rows = step_rows.loc[
        (step_rows['now'] > (i-1) * step)]
    step_rows.to_csv(
        '%s\\%s' % (root_path, str(i) + '_usage_step.csv'),
        encoding='utf-8', index=False)
