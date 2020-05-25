import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from numpy import genfromtxt

merged_file = "1_step.csv"
column = "elapsed"

df=pd.read_csv(merged_file, sep=',',header=0)
column_values = df[column].values


k2, p = stats.normaltest(column_values)

print('asdasd')