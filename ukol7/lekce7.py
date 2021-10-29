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

from scipy.stats import norm
seaborn.distplot(df["prodejni_cena_mil"], fit=norm).set_title("Distribution plot")
(mu, sigma) = stats.norm.fit(df["prodejni_cena_mil"])
print ("mu={0}, sigma={1}".format(mu, sigma))
plt.ylabel("Frequency") # y label

plt.legend(["Normal dist. ($\mu=$ {:.2f} and $\sigma=$ {:.2f} )".format(mu, sigma)],loc="best")
plt.show()