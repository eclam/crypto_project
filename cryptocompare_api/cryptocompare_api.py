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

def coin_list(coins='all'):
	url_path = build_url('coinlist')

	if coins != 'all': #finds selected cryptocurrencies from the json_data 
		text_data = data_get(url_path)['Data']
		sel_data = {c: text_data[c] for c in coins}
	else:
		sel_data = data_get(url_path)['Data']

	return sel_data

def build_url(funct, **kwargs):
	url_base = "https://min-api.cryptocompare.com/data/"
	if funct == 'coinlist':
		url_root = 'all/coinlist'
	else:
		url_root = funct + '?'

		keys_data = kwargs.keys()
		for key, value in keys_data:
			if key == 'fsym':
				url_root.append('fsym={}'.format(value))
			elif key == 'fsyms':
				url_root.append('fsyms={}'.format( ','.join(value) ))
			elif key == 'tsym':
				url_root.append('tsym={}'.format(value))
			elif key == 'tsyms':
				url_root.append('tsyms={}'.format( ','.join(value) ))
			elif key == 'e' and value != 'all':
				url_root.append('e={}'.format(value))
			elif key == 'try_conversion' and not value:
				url_root.append('tryConversion=false')
			elif key == 'markets' and value != 'all':
				url_root.append('&markets={}'.format(','.join(value)))
			elif key == 'avgType' and value != 'HourVWAP':
				url_root.append('avgType={}'.format(value))
			elif key == 'UTCHourDiff' and value != 0:
				url_root.append('UTCHourDiff={}'.format(value))
			elif key == 'ts':
				url_root.append('ts={}'.format(value))
			elif key == 'aggregate' and value != 1:
				url_root.append('aggregate={}'.format(value))
			elif key == 'limit' and value != 1440:
				url_root.append('limit={}'.format(value))


	# url_path =  url_base + url_root
	url_path = url_base + url_root
	return url_path

def coin_snapshot(fsym, tsym):
	url = build_url('coinsnapshot',fsym=fsym, tsym=tsym)
	json_data = data_get(url)['Data']

	return json_data

# def price(fsym, tsyms, e): #e = exchange 

# def price_multi(fsyms, tsyms, e) #e = exchange 

# def price_multifull(fsyms, tsysms, e)

# def gen_coinavg(fsym, tsym, markets)

# def day_avg(fsym, tsym, e, toTs) #toTs = time stamp, avgType = Hour VWAP, tryconversion = get values w/o using conversion 

# def historical_price(fsym, tsyms, ts, markets)

# def coin_snapshot_ID(id)

# def social_stats(id)

# def histo_min(fsym, tsym, limit, aggregate, toTs, tryConversion, e)

# def histo_hour(fysm, tsym, limit, aggregate, toTs, tryConversion, e)

# def histo_day(fysm, tsym, limit, aggregate, toTs, tryConversion, e)

# def top_pairs(fsym, tsym, limit)