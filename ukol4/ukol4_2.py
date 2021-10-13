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
inspector = inspect(engine)

pandas.set_option('display.max_columns', None)
#df = pandas.read_sql("dreviny", con=engine)

#Pomocí SQL dotazu si připrav tabulku o krádeži motorových vozidel (sloupec PRIMARY_DESCRIPTION by měl mít hodnotu "MOTOR VEHICLE THEFT").
#Tabulku dále pomocí pandasu vyfiltruj tak, aby obsahovala jen informace o krádeži aut (hodnota "AUTOMOBILE" ve sloupci SECONDARY_DESCRIPTION).
#Ve kterém měsíci dochází nejčastěji ke krádeži auta?

crime = pandas.read_sql("SELECT * FROM \"crime\" WHERE \"PRIMARY_DESCRIPTION\" = 'MOTOR VEHICLE THEFT';", con=engine)
crime = crime[crime["SECONDARY_DESCRIPTION"] == "AUTOMOBILE"]
crime["date_converted"] = pandas.to_datetime(crime["DATE_OF_OCCURRENCE"], dayfirst=True)
crime["month"] = crime["date_converted"].dt.month
crime_sum = pandas.DataFrame(crime["month"])
crime_sum = crime_sum.groupby("month").size().reset_index(name='counts').plot.bar(x="month", y="counts", legend=True)
print(crime_sum)
plt.show()