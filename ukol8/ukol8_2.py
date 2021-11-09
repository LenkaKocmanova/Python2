import requests
import pandas
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

#r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/MLTollsStackOverflow.csv")
#with open("MLTollsStackOverflow.csv", "wb") as f:
#  f.write(r.content)

pandas.set_option('display.max_columns', None)
df = pandas.read_csv("MLTollsStackOverflow.csv")
#print(df.head())
python_df = df[["month", "python"]]
python_df = python_df.set_index("month")
print(python_df.head())
python_df.plot()

decompose = seasonal_decompose(python_df['python'], model='multiplicative', period=12)
decompose.plot()


mod = ExponentialSmoothing(python_df["python"], seasonal_periods=12, trend="add", seasonal="add", use_boxcox=True, initialization_method="estimated",)
res = mod.fit()
df["HM"] = res.fittedvalues
#df[["HM", "python"]].plot()
df_forecast = pandas.DataFrame(res.forecast(12), columns=["Prediction"])
df_with_prediction = pandas.concat([df, df_forecast])
df_with_prediction[["python", "Prediction"]].plot()
plt.show()
