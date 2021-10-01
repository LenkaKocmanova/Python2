import requests
import pandas

#r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/dopravni-urazy.csv")
#open("dopravni-urazy.csv", "wb").write(r.content)

#r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/kraje.csv")
#open("kraje.csv", "wb").write(r.content)

#r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/sportoviste.json")
#open("sportoviste.json", "wb").write(r.content)

#r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/adopce-zvirat.csv")
#open("adopce-zvirat.csv", "wb").write(r.content)

zvirata = pandas.read_csv("adopce-zvirat.csv", sep=";")
print(zvirata.shape)
zvirata = zvirata.dropna(how="all", axis="columns")
print(zvirata.shape)
zvirata = zvirata.dropna(how="all", axis=0)
print(zvirata.shape)
pandas.set_option('display.max_columns', None)
print(zvirata.head())

for ad in zvirata.itertuples():
    kod_kraje = zvirata.cena
    nazev_kraje = zvirata.k_prohlidce
    nase = zvirata[(zvirata["cena"] <= kod_kraje)]["hodnota"].mean()
#nase = zvirata[(zvirata["cena"]<=2500) & (zvirata["k_prohlidce"] == 1.0)]
print(nase.shape)
print(nase.head())
