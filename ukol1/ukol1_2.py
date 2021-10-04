import pandas
import requests
import numpy

df = pandas.read_csv("london_merged.csv")
df_w = pandas.read_csv("weather.csv")
pandas.set_option('display.max_columns', None)


df["timestamp"] = pandas.to_datetime(df["timestamp"])
df["year"] = df["timestamp"].dt.year

soucet = df["cnt"].sum()
print("Soucet je {0}".format(soucet))
df_grouped = df.groupby(["year","weather_code"])["cnt"].sum()
df_grouped = df_grouped.reset_index()


df_joined = pandas.merge(df_grouped, df_w, on=["weather_code"])
df_pivot = pandas.pivot_table(df_joined, index = "year", columns="weather_string", values="cnt", aggfunc=numpy.sum, margins = True)

print(df_pivot)

df_pivot_percentage = df_pivot.div( df_pivot.iloc[:,-1], axis=0 )*100
print(df_pivot_percentage)