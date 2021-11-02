import pandas
import requests
import matplotlib.pyplot as plt
import seaborn
import statsmodels.formula.api as smf

#r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/Concrete_Data_Yeh.csv")
#with open("Concrete_Data_Yeh.csv", "wb") as f:
#  f.write(r.content)

pandas.set_option('display.max_columns', None)
df = pandas.read_csv("Concrete_Data_Yeh.csv")
print(df.head())

seaborn.heatmap(df.corr(), annot=True, linewidths=.5, fmt=".2f", cmap="Blues", vmax=1)
#plt.show()
mod = smf.ols(formula="csMPa ~ cement + slag + flyash + water + superplasticizer + coarseaggregate + fineaggregate"
                      " + age", data=df)
res = mod.fit()
#print(res.summary())
# přesnost modelu je 0.616. To není dobré. Koeficient vody vyšel záporný.
# Dalo se to vyčíst už z teplotní mapy, proto vodu odstraním.
mod = smf.ols(formula="csMPa ~ cement + slag + flyash + superplasticizer + coarseaggregate + fineaggregate"
                      " + age", data=df)
res = mod.fit()
print(res.summary())
# Přesnost modelu se trochu snížila (na 0.610). Voda neměla téměř vliv na model.