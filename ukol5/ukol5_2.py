import requests
import pandas
import numpy
import statistics

#r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/crypto_prices.csv")
#open("crypto_prices.csv", "wb").write(r.content)

df = pandas.read_csv("crypto_prices.csv")
pandas.set_option('display.max_columns', None)

df["Rank"] = df.groupby(["Name"])["Date"].rank(method="min")
df_bitcoin = df[df["Name"] == "Bitcoin"]
df_bitcoin = df_bitcoin.sort_values(["Rank"])
print(df_bitcoin)
df_bitcoin["preview"] = df_bitcoin["Close"].shift()
df_bitcoin["change"] = numpy.where((df_bitcoin["Rank"] != 1.0), ((df_bitcoin["Close"] - df_bitcoin["preview"])/df_bitcoin["preview"])+1, "NaN")
df_bitcoin = df_bitcoin.iloc[1:]
print(df_bitcoin)
seznam = []
seznam = df_bitcoin["change"].astype(float).tolist()

print((statistics.geometric_mean(seznam))-1)