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