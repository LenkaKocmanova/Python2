import requests
import pandas

#r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/lexikon-zvirat.csv")
#open("lexikon-zvirat.csv", "wb").write(r.content)

zvirata = pandas.read_csv("lexikon-zvirat.csv", sep=";")
print(zvirata.shape)
zvirata = zvirata.dropna(how="all", axis="columns")
print(zvirata.shape)
zvirata = zvirata.dropna(how="all", axis=0)
print(zvirata.shape)
zvirata = zvirata.set_index("id")
#pandas.set_option('display.max_columns', None)
#print(zvirata.head())

def popisek(radek):
    zprava = "{0} preferuje následující typ stravy: {1}. ".format(radek.title, radek.food)
    zprava += "Konkrétně ocení když mu do misky přistanou {0}. \nJak toto zvíře poznáme: {1}".format(radek.food_note, radek.description)
    return zprava

zvirata["popisek"] = zvirata.apply(popisek, axis=1)
print(zvirata["popisek"][320])
print(zvirata["popisek"][300])