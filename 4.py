import pandas as pd

import sweetviz as sv

df = pd.read_csv(r"C:\Users\annah\Downloads\train.csv")

a_rep = sv.analyze(df)

a_rep.show_html()
