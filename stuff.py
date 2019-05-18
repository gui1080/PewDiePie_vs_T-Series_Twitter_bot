import urllib.request
import json
import time
import tweepy


def data(key, content):
	data_url = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+content+"&key="+key).read()
	subs = json.loads(data_url)["items"][0]["statistics"]["subscriberCount"]

	return subs



def first_data_update(key, good_content, bad_content):
	 
	pewds_last_update = data(key, good_content)

	tseries_last_update = data(key, bad_content)

	subgap_last_update = (int(pewds_last_update)) - (int(tseries_last_update)) 

	return subgap_last_update 
