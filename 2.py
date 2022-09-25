import pandas as pd

from dataprep.eda import create_report

df = pd.read_csv(r"C:\Users\annah\Downloads\train.csv")

report = create_report(df)

report.save(r"C:\Users\annah\Downloads")