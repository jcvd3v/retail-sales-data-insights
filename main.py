import pandas as pd
df = pd.read_csv("data\sales.csv", encoding="utf-8", header=0, index_col=0)

print(df.head())