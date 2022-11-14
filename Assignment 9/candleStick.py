import yfinance as yf
import  mplfinance as mpf
import  pandas as pd

stock_ticker=input('Enter the stock ticker = ').upper()
time_period=input('Enter the time period = ')
time_interval=input('Enter the time interval = ')

data=yf.download(tickers=stock_ticker,period=time_period,interval=time_interval)
data=pd.DataFrame(data)

data.drop(data.columns[[4,5]],axis=1,inplace=True)
print(data)

mpf.plot(
    data,
    type="candle",
    style='yahoo',
    title=stock_ticker
)