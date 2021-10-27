import requests
import pandas
from scipy.stats import mannwhitneyu
from scipy.stats import norm

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/psenice.csv") as r:
  open("psenice.csv", 'w', encoding="utf-8").write(r.text)
# nulová hypotéza: Zrna jsou stejně velká
# alternativní hypotéza: Zrna jedné odrůdy jsou větší než druhé nebo naopak
df = pandas.read_csv("psenice.csv")
pandas.set_option('display.max_columns', None)
x = df["Rosa"]
y = df["Canadian"]
print(mannwhitneyu(x, y))
# výsledek je p-value = 3*10^-24
# nulovou hypotézu zamítáme
