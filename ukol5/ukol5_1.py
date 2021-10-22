import requests
import pandas
import numpy

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/crypto_prices.csv")
open("crypto_prices.csv", "wb").write(r.content)

df = pandas.read_csv("crypto_prices.csv")
pandas.set_option('display.max_columns', None)
#print(df.head())

df["Rank"] = df.groupby(["Name"])["Date"].rank(method="min")
#print(df)
df["preview"] = df["Close"].shift()
df["percentage"] = numpy.where((df["Rank"] != 1.0), (df["Close"] - df["preview"])* 100 / df["preview"], "NaN")
#print(df)
df1 = df[df["percentage"] != "NaN"]
#print(df1)
seznam = df["Name"].unique()
print(seznam)
print(df1.shape[0])
print(type(df1))
#print((df1["Name"], df1["Date"]).nunique())
df1 = df1.drop_duplicates(ignore_index=True)
df_pivot = pandas.pivot_table(df1, values="percentage", index="Date", columns="Name", aggfunc=numpy.max)
print(type(df_pivot))
#df_pivot.columns = df_pivot.columns.droplevel(0) #remove amount
df_pivot.columns.name = None               #remove categories
df_pivot = df_pivot.reset_index()                #index to columns
df_pivot = df_pivot.astype(float)
df_correl = df_pivot.corr()
print(df_correl)
