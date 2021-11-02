import pandas
import requests
import matplotlib.pyplot as plt
import seaborn
import statsmodels.formula.api as smf

#r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/Fish.csv")
#with open("Fish.csv", "wb") as f:
#  f.write(r.content)

pandas.set_option('display.max_columns', None)
df = pandas.read_csv("Fish.csv")
print(df.head())

mod = smf.ols(formula="Weight ~ Length2", data=df)
res = mod.fit()
#print(res.summary())
plt.plot(df["Length2"], df["Weight"], "b.")
plt.plot(df["Length2"], res.fittedvalues, "r")
plt.show()
# přesnost modelu je 0.844

mod = smf.ols(formula="Weight ~ Length2 + Height", data=df)
res = mod.fit()
#print(res.summary())
# přesnost modelu se zvýšila na 0.875

druh = df.groupby('Species')['Weight'].mean()
#print(druh)
df['Druhy_prum_hm'] = df['Species'].map(druh)
mod = smf.ols(formula="Weight ~ Length2 + Height + Druhy_prum_hm", data=df)
res = mod.fit()
print(res.summary())
# přesnost modelu se zvýšila na 0.9
