import requests


def update_champions():
	return

def update_spells():
	return

def update_items():
	url = "http://ddragon.leagueoflegends.com/cdn/9.23.1/data/en_US/item.json"
	r = requests.get(url,{})
	data = r.json()
	items = []
	for item in list(data["data"].keys()):
		temp = (item, data["data"][item]["name"])
		items.append(temp)


def update_runes():
	return

def patch():
	update_champions()
	update_spells()
	update_items()
	update_runes()
	return

update_items()