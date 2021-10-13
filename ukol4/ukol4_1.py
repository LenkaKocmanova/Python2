import os
import pandas
import psycopg2
from sqlalchemy import create_engine, inspect
import matplotlib.pyplot as plt

HOST = "czechitaspsql.postgres.database.azure.com"
PORT = 5432

USER = "lenka.kocmanova"
USERNAME = f"{USER}@czechitaspsql"
DATABASE = "postgres"
PASSWORD = ""

engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}", echo = True)

#engine = create_engine("sqlite:///:memory:")
#engine = create_engine("sqlite:///databaze.db")

inspector = inspect(engine)
#print(inspector.get_table_names())

pandas.set_option('display.max_columns', None)
#df = pandas.read_sql("dreviny", con=engine)

smrk = pandas.read_sql("SELECT * FROM \"dreviny\" WHERE dd_txt = 'Smrk' OR dd_txt = 'Jedle' OR dd_txt = 'Douglaska';", con=engine)
print(smrk)

nahodila_tezba = pandas.read_sql("SELECT * FROM \"dreviny\" WHERE druhtez_txt = 'Nahodilá těžba dřeva';", con=engine)
#print(nahodila_tezba)

nahodila_tezba_aggregated = nahodila_tezba.groupby(["prictez_txt"])["hodnota"].sum()
nahodila_tezba_aggregated = pandas.DataFrame(nahodila_tezba_aggregated)
nahodila_tezba_aggregated = nahodila_tezba_aggregated.reset_index()
print(nahodila_tezba_aggregated)
nahodila_tezba_aggregated.sort_values(by="hodnota").plot.bar(x="prictez_txt", y="hodnota", legend=True)
plt.show()