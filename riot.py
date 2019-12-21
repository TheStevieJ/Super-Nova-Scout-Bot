import requests
import sys
from pprint import pprint

def load_key():
	file = open("key.txt","r")
	return file.readline()


def get_match(match_id):
	url = "https://na1.api.riotgames.com/lol/match/v4/matches/" + str(match_id) + "?"
	data = api_request(url)
	return data


def get_summoner(name):
	url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name + "?"
	data = api_request(url)
	return data["accountId"]


def attach_key(pre_url):
	return pre_url + "api_key=" + load_key()


def api_request(url):
	url = attach_key(url)
	r = requests.get(url,{})
	data = r.json()
	if 'status' in data:
		sys.exit("Riot API request failed with error code " + str(data["status"]['status_code']) + ": " + data["status"]["message"] + "\nFrom request: " + url)
	return data