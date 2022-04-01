import pyupbit

access_key = "hryAOD0pNpTRwFkcRCmcTeVJwtn52gD3aK2nDZpX"
secret_key = "ImqRderQ00C07qnawHkxqmzwVRsCCxfIpwUjky3c"

upbit = pyupbit.Upbit(access_key, secret_key)
print(upbit.get_balances(True))
print('')

# 잔고 조회 : 인자 없이 호출 시 [1] 번째 튜플 안넘어옴 (False 가 디폴트)
# [1] : 초당/분당 호출 가능 수를 확인 데이터
# [
# {'currency': 'KRW', 'balance': '0.70164652', 'locked': '0.0', 'avg_buy_price': '0',
# 'avg_buy_price_modified': True, 'unit_currency': 'KRW'},
# {'currency': 'BTT', 'balance': '0.0', 'locked': '157479380.12954', 'avg_buy_price':# '0.006',
# 'avg_buy_price_modified': False, 'unit_currency': 'KRW'},
# {'currency': 'APENFT', 'balance':'1155265.04051467', 'locked': '0.0', 'avg_buy_price': '0',
# 'avg_buy_price_modified': False, 'unit_currency': 'KRW'},
# {'currency': 'SGB', 'balance': '1399.02508129', 'locked': '0.0', 'avg_buy_price': '0',
# 'avg_buy_price_modified': False, 'unit_currency': 'KRW'},
# {'currency': 'CELO', 'balance': '25.40026047', 'locked': '0.0', 'avg_buy_price': '3935',
# 'avg_buy_price_modified': False, 'unit_currency': 'KRW'}
# ], {'group': 'default', 'min': 899, 'sec': 29})


