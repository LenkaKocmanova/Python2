import yfinance as yf
import pandas
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.graphics.tsaplots import plot_acf

pandas.set_option('display.max_columns', None)
csco = yf.Ticker("CSCO")
csco_df = csco.history(period="5y")
csco_close = csco_df[["Close"]]
plot_acf(csco_close["Close"])

model = AutoReg(csco_close['Close'], lags=10, trend="c", seasonal=True, period=7)
model_fit = model.fit()

predictions = model_fit.predict(start=csco_close.shape[0], end=csco_close.shape[0] + 5)
df_forecast = pandas.DataFrame(predictions, columns=["Prediction"])
df_with_prediction = pandas.concat([csco_df, df_forecast])
df_with_prediction_end = df_with_prediction.tail(55)
df_with_prediction_end[["Close", "Prediction"]].plot()
plt.show()

