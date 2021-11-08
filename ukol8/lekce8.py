import pandas
import matplotlib.pyplot as plt
import requests

#r = requests.get("https://raw.githubusercontent.com/pesikj/python-032021/master/02_statistika/04/AirPassengers.csv?token=ALBCQKSCNFNESO24WOKXUZDBRDCX6")
#open("AirPassengers.csv", "wb").write(r.content)

df = pandas.read_csv("AirPassengers.csv")
df = df.rename({"#Passengers": "Passengers"}, axis=1)
df = df.set_index("Month")
#print(df.head())

df["SMA_12"] = df["Passengers"].rolling(12, min_periods=1).mean()
df[["SMA_12", "Passengers"]].plot()

#exponencialni vyrovnani EMA_t = alpha*x_t + (1 - alpha)EMA_t-1
df["EMA"] = df["Passengers"].ewm(alpha=0.1).mean()
df[["EMA", "Passengers"]].plot()

#predikce
from statsmodels.tsa.holtwinters import ExponentialSmoothing
mod = ExponentialSmoothing(df["Passengers"], seasonal_periods=12, trend="add", seasonal="add", use_boxcox=True, initialization_method="estimated",)
res = mod.fit()
df["HM"] = res.fittedvalues
df[["HM", "Passengers"]].plot()

df_forecast = pandas.DataFrame(res.forecast(24), columns=["Prediction"])
df_with_prediction = pandas.concat([df, df_forecast])
df_with_prediction[["Passengers", "Prediction"]].plot()

print(df["Passengers"].autocorr(lag=1))

from statsmodels.tsa.seasonal import seasonal_decompose

#rozdeleni dat
decompose = seasonal_decompose(df['Passengers'], model='additive', period=12)
decompose.plot()

from statsmodels.tsa.ar_model import AutoReg

model = AutoReg(df['Passengers'], lags=12, trend="c", seasonal=True, period=12)
model_fit = model.fit()
predictions = model_fit.predict(start=df.shape[0], end=df.shape[0] + 12)
df_forecast = pandas.DataFrame(predictions, columns=["Prediction"])
df_with_prediction = pandas.concat([df, df_forecast])
df_with_prediction[["Passengers", "Prediction"]].plot()
plt.show()