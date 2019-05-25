#created by Zach Friedman with help from https://pythonprogramming.net/getting-stock-prices-python-programming-for-finance/

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2000, 1, 1)
end = dt.datetime.now()

df1 = web.DataReader('VOO', 'yahoo', start, end)
df2 = web.DataReader('AAPL', 'yahoo', start, end)
df3 = web.DataReader('AMZN', 'yahoo', start, end)

print("\nVOO - Vanguard S&P 500 ETF")
print(df1.tail())
print("\nAAPL - Apple Inc.")
print(df2.tail())
print("\nAMZN - Amazon Inc.")
print(df3.tail())
