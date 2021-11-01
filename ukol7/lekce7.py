import requests
import pandas
import matplotlib.pyplot as plt
import seaborn
from scipy import stats

#r = requests.get("https://raw.githubusercontent.com/pesikj/python-032021/master/02_statistika/03/ceny_domu.csv?token=ALBCQKT2625WJ5SGGFIBI6TBPPALQ")
#open("ceny_domu.csv", "wb").write(r.content)

df = pandas.read_csv("ceny_domu.csv")
pandas.set_option('display.max_columns', None)
#print(df.head())

import statsmodels.formula.api as smf

mod = smf.ols(formula="prodejni_cena_mil ~ obytna_plocha_m2", data=df)
res = mod.fit()
#print(res.summary())

df.isna().sum()
df["plocha_pozemku_pred_domem_m2"] = df["plocha_pozemku_pred_domem_m2"].fillna(0)
seaborn.heatmap(df.corr(), annot=True, linewidths=.5, fmt=".2f", cmap="Blues", vmax=1)
plt.show()
df = df.drop("pocet_aut_v_garazi", axis=1)
df = df.drop("plocha_pozemku_pred_domem_m2", axis=1)
df = df.drop("plocha_pozemku_m2", axis=1)

mod = smf.ols(formula="prodejni_cena_mil ~ obytna_plocha_m2 + celkova_kvalita + rok_vystavby + rok_rekonstrukce "
                      " + plocha_garaze_m2 + pocet_koupelen", data=df)
res = mod.fit()
res.summary()
mod = smf.ols(formula="prodejni_cena_mil ~ obytna_plocha_m2 + celkova_kvalita + rok_vystavby + rok_rekonstrukce "
                      " + plocha_garaze_m2", data=df)
res = mod.fit()
res.summary()

#predikce
data = pandas.DataFrame({"obytna_plocha_m2": [200],
                         "celkova_kvalita": [8],
                         "rok_vystavby": [1980],
                         "rok_rekonstrukce": [2010],
                         "plocha_garaze_m2": [60]})
print(res.predict(data))

from scipy.stats import norm
seaborn.distplot(df["prodejni_cena_mil"], fit=norm).set_title("Distribution plot")
(mu, sigma) = stats.norm.fit(df["prodejni_cena_mil"])
print ("mu={0}, sigma={1}".format(mu, sigma))
plt.ylabel("Frequency") # y label

plt.legend(["Normal dist. ($\mu=$ {:.2f} and $\sigma=$ {:.2f} )".format(mu, sigma)],loc="best")
plt.show()