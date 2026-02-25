import numpy as np
import pandas as pd

df = pd.read_csv("Countries.csv")
print(df)

# ---------Which country has the highest population
# print(df.columns.value_counts())
print(df.columns)

print(df[df["population"]==df["population"].max()])

# -----------what is the capital of the country with highest population
print(df[df["population"]==df["population"].max()]["capital_city"])

# which country has the least population
print(df[df["population"]== df["population"].min()]["country"])

# give me top countries with highest democratic score
print(df[df["democracy_score"].max()]["country"])

# how many total regions are there
# how many countries lies in eastern Europe Region
