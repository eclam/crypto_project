#	Cryptocurrency Self project by Eric Lam
#	Implementing Cryptochart API 
#	URL Link for API: 		http://api.cryptocoincharts.info/ 
#	License:				GPL 
#	Email: 					Ericlam2012@live.com 
#	Python Ver:			 	Python 3 + Anaconda 

import json
import requests
import sys

def data_get(url):
	# (For example) url = "https://min-api.cryptocompare.com/" + 'listCoins'
	try:
		json_data = requests.get(url, timeout=2).json()

	except requests.exceptions.HTTPError as http_err:
		print('HTTP Error: ', http_err)
		sys.exit(1)
	except requests.exceptions.ConnectionError as conn_error:
		print('Cannot Connect Error: ', conn_error)
		sys.exit(1)
	except requests.exceptions.Timeout as timedout_err:
		print("Timed Out Error: ",timedout_err)
		data_get(url, link)
	except requests.exceptions.RequestException as err:
		print("Error: ", err)
		sys.exit(1)

	return json_data

# def url_build():



def coin_list(coins='all'):
	url_path = "https://min-api.cryptocompare.com/data/all/coinlist"

	if coins != 'all': #finds selected cryptocurrencies from the json_data 
		text_data = data_get(url_path)['Data']
		text_data = {c: text_data[c] for c in coins}
	else:
		text_data = data_get(url_path)['Data']

	return text_data



