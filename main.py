import requests
import pandas
import numpy

#r = requests.get("https://raw.githubusercontent.com/pesikj/python-032021/master/01_pandas/01/ukol/london_merged.csv?token=ALBCQKQ7TMDMXG4ABDQRB73BJHF72")
#open("london_merged.csv", 'wb').write(r.content)

#r = requests.get("https://raw.githubusercontent.com/pesikj/python-032021/master/01_pandas/01/ukol/tested.csv?token=ALBCQKUCTSQ2TQLRAIFR6VDBJHF24")
#open("tested.csv", 'wb').write(r.content)

df = pandas.read_csv("tested.csv")
len(df)
print(df.head())
for i in range(len(df)):
    if df["Sex"][i] == "male":
        print(i)
        df["male"] = 1
        df["female"] = 0
    else:
        df["male"] = 1
        df["female"] = 0
df_aggregated = df.groupby(["Pclass", "Survived"])["male"].sum()
df_aggregated = pandas.DataFrame(df_aggregated)
print(df.head())
#print(df_aggregated.head())
#df_pivot = pandas.pivot_table(df, values="male", index="Pclass", columns="Survived", aggfunc=numpy.sum, margins=True)
#print(df_pivot)