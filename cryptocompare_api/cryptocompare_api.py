#  Cryptocurrency Self project by Eric Lam 
#  License: GPL 
#  Email: CKELAM@outlook.com 
#  Implementing Cryptochart API 
# http://api.cryptocoincharts.info/listCoins


import json
import requests


def data_get(url, link):
	# url = cc_charts_path + 'listCoins'
	url_path = url + link
	try:
		resp = requests.get(url_path)
		json_data = resp.json()

	except Exception as e: 
		print('Connection Failed')
		print(e)



cc_charts_path = "https://min-api.cryptocompare.com/"
data_get(cc_charts_path,'')

# print(json_data)


