import requests
import pandas
import numpy

#with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/air_polution_ukol.csv") as r:
#  open("air_polution_ukol.csv", 'w', encoding="utf-8").write(r.text)

pandas.set_option('display.max_columns', None)
polution = pandas.read_csv("air_polution_ukol.csv")
print(polution.dtypes)
polution["date"] = pandas.to_datetime(polution["date"])
polution["year"] = polution["date"].dt.year
polution["month"] = polution["date"].dt.month
polution_pivot = pandas.pivot_table(polution, index = "year", columns="month", values= "pm25", aggfunc="mean", margins = True)
print(polution.dtypes)
print(polution.head())
print(polution_pivot)