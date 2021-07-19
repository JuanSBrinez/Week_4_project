import pandas as pd
import yfinance as yf
import pandas_datareader as web
import datetime
import matplotlib.pyplot as plt

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2013, 1, 27)
gdp = web.DataReader('GDP', 'fred', start, end)
print(gdp)

inflation = web.DataReader(['CPIAUCSL', 'CPILFESL'], 'fred', start, end)
print(inflation.head())

inflation.plot()
plt.savefig('website/static/FREDTEST.png')