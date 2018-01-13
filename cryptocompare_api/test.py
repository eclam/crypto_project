# from cryptocompare_api import coin_list, data_get, build_url
from cryptocompare_api import *
import json


# print( build_url('price') )
# print( build_url('coinlist'))

# text_data = coin_list( coins='all' ) #feed list of wanted coins through coins = []

print(coin_snapshot("LTC","CAD"))


# for key, value in text_data.items():
# 	print(key, value)
# 	count+=1
# 	print(count)
# json_data = {c:text_data[c] for c in ['ETC','BTC', 'XRP']}
# print(json_data)

# print(json.dumps(text_data))
# keys_data = text_data.keys() # takes all the keys from said library 

# print( list(text_data.keys())[:20] ) #prints the first few keys

# for key in keys_data:
	# print(json.dumps(text_data[key]),key)


# url_path = "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR"
# json_data = data_get(url_path)
# print(json_data)


#############################################################
#might need this code in future? 

# cc_charts_path = "https://min-api.cryptocompare.com/"
# json_data = data_get_cc(cc_charts_path,'')

# def data_get_cc(url):
# 	# (For example) url = "https://min-api.cryptocompare.com/" + 'listCoins'
# 	try:
# 		resp = requests.get(url, timeout=2).text.encode('utf-8')
# 		json_data = json.loads(resp)

# 	except requests.exceptions.HTTPError as http_err:
# 		print('HTTP Error: ', http_err)
# 		sys.exit(1)
# 	except requests.exceptions.ConnectionError as conn_error:
# 		print('Cannot Connect Error: ', conn_error)
# 		sys.exit(1)
# 	except requests.exceptions.Timeout as timedout_err:
# 		print("Timed Out Error: ",timedout_err)
# 		data_get(url, link)
# 	except requests.exceptions.RequestException as err:
# 		print("Error: ", err)
# 		sys.exit(1)

# 	return json_data
#############################################################