import requests
import pandas
from scipy.stats import mannwhitneyu
from scipy.stats import norm

#with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/air_polution_ukol.csv") as r:
#  open("air_polution_ukol.csv", 'w', encoding="utf-8").write(r.text)

pandas.set_option('display.max_columns', None)
polution = pandas.read_csv("air_polution_ukol.csv")
polution["date"] = pandas.to_datetime(polution["date"])
polution["year"] = polution["date"].dt.year
polution["month"] = polution["date"].dt.month
polution19 = polution[(polution["year"] == 2019) & (polution["month"] == 1)]["pm25"]
polution20 = polution[(polution["year"] == 2020) & (polution["month"] == 1)]["pm25"]
# nulová hypotéza: Znečištění bylo v obou letech stejné
# alternativní hypotéza: Znečištění bylo v prvním roce větší než ve druhém, nebo naopak
U, p = mannwhitneyu(polution19, polution20)
print(p)
# nulovou hypotézu nezamítáme