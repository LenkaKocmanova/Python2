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

def check_url(radek):
    if not (isinstance(radek.image_src, str)):
        return radek.title
    if not (radek.image_src.startswith("https://zoopraha.cz/images/")):
        return radek.title
    delka = len(radek.image_src)
    koncovka = radek.image_src[delka - 3:delka]
    if not ((koncovka == "jpg") | (koncovka == "JPG")):
        return radek.title

for zv in zvirata.itertuples():
    if (check_url(zv)):
        print(check_url(zv))