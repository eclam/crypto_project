#	Cryptocurrency Self project by Eric Lam
#	Implementing Cryptochart API 
#	URL Link for API: 		http://api.cryptocoincharts.info/ 
#	License:				GPL 
#	Email: 					Ericlam2012@live.com 
#	Python Ver:			 	Python 3 + Anaconda 

import json
import requests
import sys

def data_get(url, link):
	# (For example) url = "https://min-api.cryptocompare.com/" + 'listCoins'
	url_path = url + link

	try:
		resp = requests.get(url_path, timeout=2)
		print(resp.raise_for_status())
		json_data = resp.json()		
	except requests.exceptions.HTTPError as http_err:
		print('HTTP Error: ', http_err)
		sys.exit(1)
	except requests.exceptions.ConnectionError as conn_error:
		print('Cannot Connect Error: ', conn_error)
		# sys.exit(1)
		data_get(url, link)
	except requests.exceptions.Timeout as timedout_err:
		print("Timed Out Error: ",timedout_err)
		data_get(url, link)
	except requests.exceptions.RequestException as err:
		print("Error: ", err)
		sys.exit(1)
 	
	return json_data


cc_charts_path = "https://min-api.cryptocompare.com/"
json_data = data_get(cc_charts_path,'')

print(json_data)


