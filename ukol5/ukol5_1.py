import requests
import pandas
import numpy
import matplotlib.pyplot as plt
#import yfinance as yf

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/crypto_prices.csv")
open("crypto_prices.csv", "wb").write(r.content)

df = pandas.read_csv("crypto_prices.csv")
pandas.set_option('display.max_columns', None)
#print(df.head())

df["Rank"] = df.groupby(["Name"])["Date"].rank(method="min")
#print(df)
df["preview"] = df["Close"].shift()
df["percentage"] = numpy.where((df["Rank"] != 1.0), (df["Close"] - df["preview"])* 100 / df["preview"], "NaN")
print(df)
df1 = df[df["percentage"] != "NaN"]
df1 = df1.drop_duplicates(ignore_index=True)
df_pivot = pandas.pivot_table(df1, values="percentage", index="Date", columns="Name", aggfunc=numpy.max)
df_pivot.columns.name = None               #remove categories
df_pivot = df_pivot.reset_index()                #index to columns
#print(df_pivot)
df_pivot_bd = df_pivot.loc[:, df_pivot.columns != "Date"]
df_pivot_bd = df_pivot_bd.astype(float)
df_correl = df_pivot_bd.corr()
print(df_correl)

corr_max = 0
corr_min = 1
for i in range(len(df_correl)):
    for j in range(i):
        if (df_correl.iloc[i, j] > corr_max):
            corr_max = df_correl.iloc[i, j]
            imax = i
            jmax = j
        if (abs(df_correl.iloc[i, j]) < corr_min):
            corr_min = df_correl.iloc[i, j]
            imin = i
            jmin = j
print("corr_max je {0} i {1} j {2}".format(corr_max, imax, jmax))
print("corr_min je {0} i {1} j {2}".format(corr_min, imin, jmin))
{df_pivot.columns.get_loc(c): c for idx, c in enumerate(df_pivot.columns)}

df_max = df_pivot.loc[:, [df_pivot.columns[imax+1], df_pivot.columns[jmax+1]]]
df_min = df_pivot.loc[:, [df_pivot.columns[imin+1], df_pivot.columns[jmin+1]]]
df_max = df_max.astype(float)
df_min = df_min.astype(float)
{df_max.columns.get_loc(c): c for idx, c in enumerate(df_max.columns)}
{df_min.columns.get_loc(c): c for idx, c in enumerate(df_min.columns)}


import seaborn
seaborn.jointplot(df_max.columns[0], df_max.columns[1], df_max.dropna(), kind='scatter', color='seagreen')
plt.show()
seaborn.jointplot("Tether", "Binance Coin", df_min.dropna(), kind='scatter', color='seagreen')
plt.show()





