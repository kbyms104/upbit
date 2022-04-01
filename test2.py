# conda install -c conda-forge ta-lib
import talib as ta
import pyupbit
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_finance import candlestick_ohlc

#pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

ticker = "KRW-BTC"
df = pyupbit.get_ohlcv(ticker, interval='day', count=200)

#print(df)

#단순 이동평균선 구하는건 한줄로 끝!
close = df['close']
df['MA5'] = close.rolling(5).mean()
df['MA20'] = ta.SMA(close, 20)
df['RSI'] = ta.RSI(close, timeperiod=14)

print(df)

# 차트를 그려주자.
# df[['close', 'MA5', 'MA20']].plot(figsize=(12, 6))
# plt.title("Days", {"fontsize": 20})
#plt.show()


fig = plt.figure(figsize=(8, 5))
fig.set_facecolor('w')
gs = gridspec.GridSpec(2, 1, height_ratios=[3, 1])
axes = []
axes.append(plt.subplot(gs[0]))
axes.append(plt.subplot(gs[1], sharex=axes[0]))
axes[0].get_xaxis().set_visible(False)

x = np.arange(len(df.index))
ohlc = df[['open', 'high', 'low', 'close']].astype(int).values
dohlc = np.hstack((np.reshape(x, (-1, 1)), ohlc))

# 봉차트
candlestick_ohlc(axes[0], dohlc, width=0.5, colorup='r', colordown='b')

# 거래량 차트
axes[1].bar(x, df['volum'], color='k', width=0.6, align='center')

plt.tight_layout()
plt.show()