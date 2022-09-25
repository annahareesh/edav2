import pandas as pd

import pandas_profiling

df = pd.read_csv(r"C:\Users\annah\Downloads\train.csv")

pandas_profiling.ProfileReport(df)

