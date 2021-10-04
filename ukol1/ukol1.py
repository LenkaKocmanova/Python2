import pandas
import requests
import numpy

#r = requests.get("https://raw.githubusercontent.com/pesikj/python-032021/master/01_pandas/01/ukol/london_merged.csv?token=ALBCQKSTDSTXNLONKY7OKTTBJLX72")
#open("london_merged.csv", 'wb').write(r.content)

#r = requests.get("https://raw.githubusercontent.com/pesikj/python-032021/master/01_pandas/01/ukol/tested.csv?token=ALBCQKXRZXXEVMVDQ63XWWDBJLX4Q")
#open("tested.csv", 'wb').write(r.content)

df = pandas.read_csv("tested.csv")

pandas.options.mode.chained_assignment = None
df_maleU = df.loc[((df["Sex"] == "male") & (df["Survived"] == 0))]
df_maleS = df.loc[((df["Sex"] == "male") & (df["Survived"] == 1))]
df_femaleU = df.loc[((df["Sex"] == "female") & (df["Survived"] == 0))]
df_femaleS = df.loc[((df["Sex"] == "female") & (df["Survived"] == 1))]

df_maleU["SuSe"] = "nepřeživší muž"
df_maleS["SuSe"] = "přeživší muž"
df_femaleU["SuSe"] = "nepřeživší žena"
df_femaleS["SuSe"] = "přeživší žena"

df_new = pandas.concat([df_maleU, df_maleS, df_femaleU, df_femaleS], ignore_index=True)

pandas.set_option('display.max_columns', None)
df_pivot = pandas.pivot_table(df_new, index = "Pclass", columns="SuSe", values= "Sex", aggfunc="count", margins = True)

print(df_pivot)

