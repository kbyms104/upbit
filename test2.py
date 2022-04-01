# conda install -c conda-forge ta-lib
import talib as ta
import pyupbit
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

ticker = "KRW-BTC"
df = pyupbit.get_ohlcv(ticker, interval = 'minute60', count=144)

print(df)

#단순 이동평균선 구하는건 한줄로 끝!
df['MA'] = ta.SMA(df['close'], 20)

#차트를 그려주자.
df[['close','MA']].plot(figsize=(12,6))
plt.title("ETH - 6 Days", {"fontsize" : 20})
plt.show()

