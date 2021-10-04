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

urazy = pandas.read_csv("dopravni-urazy.csv", sep=";")
kraje = pandas.read_csv("kraje.csv")
urazy_prumer = pandas.DataFrame(columns=["nazev_kraje", "hodnota"])