from cryptocompare_api import *
import json

text_data = coin_list( coins='all' ) #feed list of wanted coins through coins = []


# print(coin_snapshot("LTC","CAD"))


# for key, value in text_data.items():
# 	print(key, value)
# 	count+=1
# 	print(count)
# json_data = {c:text_data[c] for c in ['ETC','BTC', 'XRP']}
# print(json_data)

print(json.dumps(text_data))
keys_data = text_data.keys() # takes all the keys from said library 

print( list(text_data.keys())[:20] ) #prints the first few keys

for key in keys_data:
	print(json.dumps(text_data[key]),key)


# url_path = "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR"
# json_data = data_get(url_path)
# print(json_data)


