#	Cryptocurrency Self project by Eric Lam
#	Implementing Cryptochart API 
#	URL Link for API: 		http://api.cryptocoincharts.info/ 
#	License:				GPL 
#	Email: 					Ericlam2012@live.com 
#	Python Ver:			 	Python 3 + Anaconda 



import json
import requests


def data_get(url, link):
	# url = cc_charts_path + 'listCoins'
	url_path = url + link
	try:
		resp = requests.get(url_path, timeout=2) #timeout subject to change
		json_data = resp.json()



	except Exception as e: 
		print('Connection Failed')
		print(e)



cc_charts_path = "https://min-api.cryptocompare.com/"
data_get(cc_charts_path,'')

# print(json_data)


