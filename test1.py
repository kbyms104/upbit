import pyupbit
print(pyupbit.Upbit)


tickers = pyupbit.get_tickers()
print(tickers)
print('')
# 티커 조회
# ['KRW-BTC', 'KRW-ETH', 'BTC-ETH', 'BTC-LTC', 'BTC-XRP', 'BTC-ETC', 'BTC-OMG', 'BTC-CVC', 'BTC-DGB', 'BTC-SC',
# 'BTC-SNT', 'BTC-WAVES', 'BTC-NMR', 'BTC-XEM', 'BTC-QTUM', 'BTC-BAT', 'BTC-LSK', 'BTC-STEEM', 'BTC-DOGE', 'BTC-BNT',
# 'BTC-XLM', 'BTC-ARDR', 'BTC-ARK', 'BTC-STORJ', 'BTC-GRS', 'BTC-REP', 'BTC-RLC', 'USDT-BTC', 'USDT-ETH', 'USDT-LTC',
# 'USDT-XRP', 'USDT-ETC', 'KRW-NEO', 'KRW-MTL', 'KRW-LTC', 'KRW-XRP', 'KRW-ETC', 'KRW-OMG', 'KRW-SNT', 'KRW-WAVES',
# 'KRW-XEM', 'KRW-QTUM', 'KRW-LSK', 'KRW-STEEM', 'KRW-XLM', 'KRW-ARDR', 'KRW-ARK', 'KRW-STORJ', 'KRW-GRS', 'KRW-REP',
# 'KRW-ADA', 'BTC-ADA', 'BTC-MANA', 'USDT-OMG', 'KRW-SBD', 'BTC-SBD', 'KRW-POWR', 'BTC-POWR', 'KRW-BTG', 'USDT-ADA',
# 'BTC-DNT', 'BTC-ZRX', 'BTC-TRX', 'BTC-TUSD', 'BTC-LRC', 'KRW-ICX', 'KRW-EOS', 'USDT-TUSD', 'KRW-TRX', 'BTC-POLY',
# 'USDT-SC', 'USDT-TRX', 'KRW-SC', 'KRW-ONT', 'KRW-ZIL', 'KRW-POLY', 'KRW-ZRX', 'KRW-LOOM', 'BTC-BCH', 'USDT-BCH',
# 'KRW-BCH', 'BTC-MFT', 'BTC-LOOM', 'KRW-BAT', 'KRW-IOST', 'BTC-RFR', 'KRW-RFR', 'USDT-DGB', 'KRW-CVC', 'KRW-IQ',
# 'KRW-IOTA', 'BTC-RVN', 'BTC-GO', 'BTC-UPP', 'BTC-ENJ', 'KRW-MFT', 'KRW-ONG', 'KRW-GAS', 'BTC-MTL', 'KRW-UPP',
# 'KRW-ELF', 'USDT-DOGE', 'USDT-ZRX', 'USDT-RVN', 'USDT-BAT', 'KRW-KNC', 'BTC-MOC', 'BTC-ZIL', 'KRW-BSV', 'BTC-BSV',
# 'BTC-IOST', 'KRW-THETA', 'BTC-DENT', 'KRW-QKC', 'BTC-ELF', 'KRW-BTT', 'BTC-IOTX', 'BTC-SOLVE', 'BTC-NKN',
# 'BTC-META', 'KRW-MOC', 'BTC-ANKR', 'BTC-CRO', 'KRW-ENJ', 'KRW-TFUEL', 'KRW-MANA', 'KRW-ANKR', 'BTC-ORBS',
# 'BTC-AERGO', 'KRW-AERGO', 'KRW-ATOM', 'KRW-TT', 'KRW-CRE', 'BTC-ATOM', 'BTC-STPT', 'KRW-MBL', 'BTC-EOS',
# 'BTC-LUNA', 'BTC-DAI', 'BTC-MKR', 'BTC-BORA', 'KRW-WAXP', 'BTC-WAXP', 'KRW-HBAR', 'KRW-MED', 'BTC-MED', 'BTC-MLK',
# 'KRW-MLK', 'KRW-STPT', 'BTC-VET', 'KRW-ORBS', 'BTC-CHZ', 'KRW-VET', 'BTC-FX', 'BTC-OGN', 'KRW-CHZ', 'BTC-XTZ',
# 'BTC-HIVE', 'BTC-HBD', 'BTC-OBSR', 'BTC-DKA', 'KRW-STMX', 'BTC-STMX', 'BTC-AHT', 'BTC-PCI', 'KRW-DKA', 'BTC-LINK',
# 'KRW-HIVE', 'KRW-KAVA', 'BTC-KAVA', 'KRW-AHT', 'KRW-LINK', 'KRW-XTZ', 'KRW-BORA', 'BTC-JST', 'BTC-CHR', 'BTC-DAD',
# 'BTC-TON', 'KRW-JST', 'BTC-CTSI', 'BTC-DOT', 'KRW-CRO', 'BTC-COMP', 'BTC-SXP', 'BTC-HUNT', 'KRW-TON', 'BTC-ONIT',
# 'BTC-CRV', 'BTC-ALGO', 'BTC-RSR', 'KRW-SXP', 'BTC-OXT', 'BTC-PLA', 'KRW-HUNT', 'BTC-MARO', 'BTC-SAND', 'BTC-SUN',
# 'KRW-PLA', 'KRW-DOT', 'BTC-SRM', 'BTC-QTCON', 'BTC-MVL', 'KRW-SRM', 'KRW-MVL', 'BTC-REI', 'BTC-AQT', 'BTC-AXS',
# 'BTC-STRAX', 'KRW-STRAX', 'KRW-AQT', 'BTC-GLM', 'KRW-GLM', 'BTC-FCT2', 'BTC-SSX', 'KRW-SSX', 'KRW-META',
# 'KRW-FCT2', 'BTC-FIL', 'BTC-UNI', 'BTC-BASIC', 'BTC-INJ', 'BTC-PROM', 'BTC-VAL', 'BTC-PSG', 'BTC-JUV', 'BTC-CBK',
# 'BTC-FOR', 'KRW-CBK', 'BTC-BFC', 'BTC-LINA', 'BTC-HUM', 'BTC-CELO', 'KRW-SAND', 'KRW-HUM', 'BTC-IQ', 'BTC-STX',
# 'KRW-DOGE', 'BTC-NEAR', 'BTC-AUCTION', 'BTC-DAWN', 'BTC-FLOW', 'BTC-STRK', 'KRW-STRK', 'BTC-PUNDIX', 'KRW-PUNDIX',
# 'KRW-FLOW', 'KRW-DAWN', 'KRW-AXS', 'KRW-STX', 'BTC-GRT', 'BTC-SNX', 'BTC-USDP', 'KRW-XEC', 'KRW-SOL', 'BTC-SOL',
# 'KRW-MATIC', 'BTC-MATIC', 'KRW-NU', 'BTC-NU', 'KRW-AAVE', 'KRW-1INCH', 'BTC-AAVE', 'BTC-1INCH', 'BTC-MASK',
# 'KRW-ALGO', 'BTC-AUDIO', 'KRW-NEAR', 'BTC-YGG', 'BTC-GTC', 'BTC-OCEAN', 'BTC-CTC', 'BTC-LPT', 'KRW-WEMIX',
# 'BTC-WEMIX', 'KRW-AVAX', 'BTC-AVAX', 'BTC-IMX', 'BTC-RNDR', 'BTC-RLY', 'KRW-T', 'BTC-T', 'KRW-CELO']

tickers = pyupbit.get_tickers(fiat="KRW")
print(tickers)
print('')
# 티커 조회
# ['KRW-BTC', 'KRW-ETH', 'KRW-NEO', 'KRW-MTL', 'KRW-LTC', 'KRW-XRP', 'KRW-ETC', 'KRW-OMG', 'KRW-SNT', 'KRW-WAVES',
# 'KRW-XEM', 'KRW-QTUM', 'KRW-LSK', 'KRW-STEEM', 'KRW-XLM', 'KRW-ARDR', 'KRW-ARK', 'KRW-STORJ', 'KRW-GRS', 'KRW-REP',
# 'KRW-ADA', 'KRW-SBD', 'KRW-POWR', 'KRW-BTG', 'KRW-ICX', 'KRW-EOS', 'KRW-TRX', 'KRW-SC', 'KRW-ONT', 'KRW-ZIL',
# 'KRW-POLY', 'KRW-ZRX', 'KRW-LOOM', 'KRW-BCH', 'KRW-BAT', 'KRW-IOST', 'KRW-RFR', 'KRW-CVC', 'KRW-IQ', 'KRW-IOTA',
# 'KRW-MFT', 'KRW-ONG', 'KRW-GAS', 'KRW-UPP', 'KRW-ELF', 'KRW-KNC', 'KRW-BSV', 'KRW-THETA', 'KRW-QKC', 'KRW-BTT',
# 'KRW-MOC', 'KRW-ENJ', 'KRW-TFUEL', 'KRW-MANA', 'KRW-ANKR', 'KRW-AERGO', 'KRW-ATOM', 'KRW-TT', 'KRW-CRE', 'KRW-MBL',
# 'KRW-WAXP', 'KRW-HBAR', 'KRW-MED', 'KRW-MLK', 'KRW-STPT', 'KRW-ORBS', 'KRW-VET', 'KRW-CHZ', 'KRW-STMX', 'KRW-DKA',
# 'KRW-HIVE', 'KRW-KAVA', 'KRW-AHT', 'KRW-LINK', 'KRW-XTZ', 'KRW-BORA', 'KRW-JST', 'KRW-CRO', 'KRW-TON', 'KRW-SXP',
# 'KRW-HUNT', 'KRW-PLA', 'KRW-DOT', 'KRW-SRM', 'KRW-MVL', 'KRW-STRAX', 'KRW-AQT', 'KRW-GLM', 'KRW-SSX', 'KRW-META',
# 'KRW-FCT2', 'KRW-CBK', 'KRW-SAND', 'KRW-HUM', 'KRW-DOGE', 'KRW-STRK', 'KRW-PUNDIX', 'KRW-FLOW', 'KRW-DAWN',
# 'KRW-AXS', 'KRW-STX', 'KRW-XEC', 'KRW-SOL', 'KRW-MATIC', 'KRW-NU', 'KRW-AAVE', 'KRW-1INCH', 'KRW-ALGO', 'KRW-NEAR',
# 'KRW-WEMIX', 'KRW-AVAX', 'KRW-T', 'KRW-CELO']

price = pyupbit.get_current_price("KRW-XRP")
print(price)
print('')
# 현재가조회
# 1005.0

price = pyupbit.get_current_price("BTC-XRP")
print(price)
print(format(price, 'f'))
print('')
# 현재가조회
# 1.829e-05
# 0.000018

price = pyupbit.get_current_price(["BTC-XRP", "KRW-XRP"])
print(price)
print('')
# 현재가조회
# {'BTC-XRP': 1.829e-05, 'KRW-XRP': 1005.0}

df = pyupbit.get_ohlcv("KRW-BTC")
print(df)
print('')

# 과거 데이터 조회
# 오전 09:00:00 기준
#    open        high  ...       volume         value
# 2021-09-14 09:00:00  54340000.0  56857000.0  ...  5994.880625  3.337047e+11
# 2021-09-15 09:00:00  56564000.0  57600000.0  ...  5204.483546  2.959247e+11
# 2021-09-16 09:00:00  57178000.0  57500000.0  ...  5358.404001  3.058392e+11
# 2021-09-17 09:00:00  57277000.0  57836000.0  ...  6908.811184  3.970425e+11
# 2021-09-18 09:00:00  57642000.0  58980000.0  ...  4935.406086  2.882914e+11
# ...                         ...         ...  ...          ...           ...
# 2022-03-28 09:00:00  55936000.0  57678000.0  ...  6374.435146  3.615686e+11
# 2022-03-29 09:00:00  56900000.0  57540000.0  ...  6629.178471  3.789075e+11
# 2022-03-30 09:00:00  56985000.0  57100000.0  ...  4136.114493  2.345294e+11
# 2022-03-31 09:00:00  56594000.0  57227000.0  ...  5141.563266  2.904254e+11
# 2022-04-01 09:00:00  55331000.0  55700000.0  ...  2470.764445  1.354481e+11
#
# [200 rows x 6 columns]

df = pyupbit.get_ohlcv("KRW-BTC", interval="minute1", count=5)
print(df)
print('')

# 과거 데이터 조회 : interval 옵션으로 월/주/일/분봉 중 하나를 선택할 수 있습니다. interval을 입력하지 않은 경우에는 내부적으로 일봉이 선택됩니다.
#                           open        high  ...    volume         value
# 2022-04-01 15:25:00  54719000.0  54778000.0  ...  2.808489  1.537204e+08
# 2022-04-01 15:26:00  54757000.0  54809000.0  ...  1.823783  9.989866e+07
# 2022-04-01 15:27:00  54795000.0  54827000.0  ...  2.060369  1.128726e+08
# 2022-04-01 15:28:00  54775000.0  54830000.0  ...  1.793960  9.828288e+07
# 2022-04-01 15:29:00  54805000.0  54826000.0  ...  0.680377  3.729131e+07
#
# [5 rows x 6 columns]

orderbook = pyupbit.get_orderbook("KRW-BTC")
print(orderbook)

bids_asks = orderbook['orderbook_units']
for bid_ask in bids_asks:
    print(bid_ask)

# 호가조회 : 매수호가(bid)와 매도호가(ask)
# {'market': 'KRW-BTC', 'timestamp': 1648795029335, 'total_ask_size': 4.29704, 'total_bid_size': 4.81057556,
# 'orderbook_units': [
# {'ask_price': 54831000.0, 'bid_price': 54829000.0, 'ask_size': 0.02771426, 'bid_size': 0.02484198},
# {'ask_price': 54832000.0, 'bid_price': 54828000.0, 'ask_size': 1.10845717, 'bid_size': 1.32506417},
# {'ask_price': 54833000.0, 'bid_price': 54827000.0, 'ask_size': 0.00322081, 'bid_size': 1.07321897},
# {'ask_price': 54835000.0, 'bid_price': 54826000.0, 'ask_size': 0.37224907, 'bid_size': 0.85156661},
# {'ask_price': 54836000.0, 'bid_price': 54825000.0, 'ask_size': 0.08176473, 'bid_size': 0.15550284},
# {'ask_price': 54841000.0, 'bid_price': 54821000.0, 'ask_size': 0.03139721, 'bid_size': 0.03724098},
# {'ask_price': 54842000.0, 'bid_price': 54820000.0, 'ask_size': 0.31554357, 'bid_size': 0.03648303},
# {'ask_price': 54850000.0, 'bid_price': 54819000.0, 'ask_size': 0.9306575, 'bid_size': 0.01044485},
# {'ask_price': 54851000.0, 'bid_price': 54816000.0, 'ask_size': 0.20104594, 'bid_size': 0.66170948},
# {'ask_price': 54854000.0, 'bid_price': 54815000.0, 'ask_size': 0.18230211, 'bid_size': 0.00346239},
# {'ask_price': 54858000.0, 'bid_price': 54809000.0, 'ask_size': 0.00953029, 'bid_size': 0.02090528},
# {'ask_price': 54860000.0, 'bid_price': 54804000.0, 'ask_size': 0.70214491, 'bid_size': 0.00776722},
# {'ask_price': 54861000.0, 'bid_price': 54800000.0, 'ask_size': 0.26781572, 'bid_size': 0.10490507},
# {'ask_price': 54862000.0, 'bid_price': 54796000.0, 'ask_size': 0.05693274, 'bid_size': 0.00526269},
# {'ask_price': 54863000.0, 'bid_price': 54791000.0, 'ask_size': 0.00626397, 'bid_size': 0.4922}
# ]}

# {'ask_price': 54779000.0, 'bid_price': 54778000.0, 'ask_size': 0.32857508, 'bid_size': 0.02251614}
# {'ask_price': 54781000.0, 'bid_price': 54777000.0, 'ask_size': 9.13e-05, 'bid_size': 0.38445911}
# {'ask_price': 54782000.0, 'bid_price': 54776000.0, 'ask_size': 0.07436808, 'bid_size': 0.18064004}
# {'ask_price': 54783000.0, 'bid_price': 54775000.0, 'ask_size': 0.08598379, 'bid_size': 0.00800794}
# {'ask_price': 54784000.0, 'bid_price': 54774000.0, 'ask_size': 0.3855667, 'bid_size': 0.04417318}
# {'ask_price': 54796000.0, 'bid_price': 54773000.0, 'ask_size': 0.002, 'bid_size': 0.06611328}
# {'ask_price': 54800000.0, 'bid_price': 54772000.0, 'ask_size': 0.00235813, 'bid_size': 0.00200832}
# {'ask_price': 54805000.0, 'bid_price': 54770000.0, 'ask_size': 0.18400112, 'bid_size': 0.59581396}
# {'ask_price': 54809000.0, 'bid_price': 54760000.0, 'ask_size': 0.00086609, 'bid_size': 0.01768061}
# {'ask_price': 54810000.0, 'bid_price': 54758000.0, 'ask_size': 0.88520119, 'bid_size': 0.0928718}
# {'ask_price': 54814000.0, 'bid_price': 54757000.0, 'ask_size': 2.26082091, 'bid_size': 0.01230566}
# {'ask_price': 54815000.0, 'bid_price': 54750000.0, 'ask_size': 0.13866594, 'bid_size': 0.08029257}
# {'ask_price': 54817000.0, 'bid_price': 54749000.0, 'ask_size': 0.03613477, 'bid_size': 0.00018254}
# {'ask_price': 54819000.0, 'bid_price': 54748000.0, 'ask_size': 0.01330109, 'bid_size': 0.01011269}
# {'ask_price': 54820000.0, 'bid_price': 54746000.0, 'ask_size': 0.38818686, 'bid_size': 0.000947}

