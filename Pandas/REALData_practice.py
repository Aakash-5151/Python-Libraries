
import pandas as pd
import numpy as np

df = pd.read_csv('anime.csv')
# print(df.head())

# print(df.loc[1]['Title'])

def extract_episode(txt):
    check = False
    data = ""
    for i in txt:
        if i == ")":
            check = False
            return data
        if check == True:
            data += i
        if i == '(':
            check = True
    

        
df["Episodes"] = df["Title"].apply(extract_episode) 
# In Episodes there is no need of "_eps" sp remove it and that will to do calculations
df["Episodes"] = df["Episodes"].str.replace(" eps","")
df["Episodes"] = df["Episodes"].astype(int)
print()
print(type(df["Episodes"]))

# print(df)
print(df.loc[0]["Title"])
print(df.loc[1]["Title"])

print(type(df.loc[0]["Episodes"]))  #here the eps numbers are in string convert them into integer

def time_extraction(txt):
    check = False
    data = ""
    for i in range(len(txt)):
        if txt[i] == ")":
            for j in range(i+1, i + 20):
                data += txt[j]
            return data
df["date"] = df["Title"].apply(time_extraction)
# print(df.head(10))
# print(df["Title"])
print(df)

# print(df.head())

#which anime has the highest score

print(df[df["Score"] == df["Score"].max()])

# give me top 5 highest scoring anime
# Which anime has the highest anime count

print(df[df["Episodes"] ==df["Episodes"].max()])
# animes with top highest episodes 
# which is longest running anime