import requests
import pandas
import numpy

#with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/1976-2020-president.csv") as r:
#  open("1976-2020-president.csv", 'w', encoding="utf-8").write(r.text)

#with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/air_polution_ukol.csv") as r:
#  open("air_polution_ukol.csv", 'w', encoding="utf-8").write(r.text)

pandas.set_option('display.max_columns', None)
president = pandas.read_csv("1976-2020-president.csv")

president = president[["state","year","state_po","state_fips","state_cen","state_ic","office","candidate","party_detailed","writein","candidatevotes","totalvotes","version","notes","party_simplified"]]
president_gr = president.sort_values([ 'year','state','candidatevotes'],ascending=False)#.groupby(['year',"state"])
president_gr["Rank"] = president_gr.groupby(["year", "state"])["candidatevotes"].rank(method="min", ascending=False)
president_1 = president_gr[president_gr["Rank"] == 1.0]
president_1 = president_1.sort_values(["state", "year"])
president_1["preview"] = president_1["party_detailed"].shift()

president_1["change"] = numpy.where((president_1["party_detailed"] != president_1["preview"])&(president_1["year"] != 1976), 1, 0)
swing = president_1.groupby("state")["change"].sum()
swing = swing.reset_index()
swing = swing.sort_values("change",ascending=False)
print(president_1.head(30))
print(swing)