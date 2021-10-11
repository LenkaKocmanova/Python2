import os

import pandas
import psycopg2
from sqlalchemy import create_engine, inspect

HOST = "czechitaspsql.postgres.database.azure.com"
PORT = 5432

USER = "lenka.kocmanova"
USERNAME = f"{USER}@czechitaspsql"
DATABASE = "postgres"
PASSWORD = "POmLav4!B273EQj7"

engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}", echo = True)

#engine = create_engine("sqlite:///:memory:")
#engine = create_engine("sqlite:///databaze.db")

inspector = inspect(engine)
#print(inspector.get_table_names())

df = pandas.read_sql(f"uzivatele-{USER}", con=engine)
#print(df)
#print(df[df["produkt"] == "sušička ovoce"]["address_street", "country"])

#df = pandas.read_sql(f"SELECT address_street, country from \"uzivatele-{USER}\" WHERE produkt = 'sušička ovoce'", con = engine)
#print(df)

def cena_produktu(radka):
    ceny = {"kávovar":2000, "šicí stroj": 5000, "topinkovač":600}
    produkt = radka["produkt"]
    return ceny.get(produkt, 1000)

df["cena"] = df.apply(cena_produktu, axis=1)
print(df)
#df.to_sql()

#nova_data = pandas.DataFrame({'name': ['Hana', 'Andrea'], 'country': ['Czech Republic', 'Czech Republic'],
#                              'address_street': ['Korunní', 'Vinohradská'], 'age': [35, 45], 'produkt': ['kávovar', 'vysavac']})

#nova_data.to_sql(f"uzivatele-{USER}", con=engine, index=False, if_exists="append")

#df= pandas.read_sql(f"uzivatele-{USER}", con=engine)
#print(df)

ob = pandas.read_sql(f"pocet_obyvatel", con=engine)
b = pandas.read_sql(f"pocet_bytu", con=engine)
##print(b.head())

spoj = pandas.merge(ob, b, on=["obec"])
spoj["pomer"] = spoj["pocet_bytu"] * 100000/ spoj["pocet_obyvatel"]
spoj = spoj.sort_values(["pomer"], ascending=False)
print(spoj)


