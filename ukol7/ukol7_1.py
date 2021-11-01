import pandas

df = pandas.read_csv("Fish.csv")

import statsmodels.formula.api as smf
print(df.corr())

mod = smf.ols(formula="Weight ~ Length1", data=df)
res = mod.fit()
print(res.summary())

mod = smf.ols(formula="Weight ~ Length1 + Length2 + Length3 + Height + Width", data=df)
res = mod.fit()
print(res.summary())