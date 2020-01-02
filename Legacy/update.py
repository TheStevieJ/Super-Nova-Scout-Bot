import requests
from database import connect_db

def get_dragon(url):
	r = requests.get(url,{})
	data = r.json()
	return data

def update_champions():
	data = get_dragon("http://ddragon.leagueoflegends.com/cdn/9.23.1/data/en_US/champion.json")
	champs = list(data["data"].keys())
	out_data = []
	for champ in champs:
		name = data["data"][champ]["id"]
		num = data["data"][champ]["key"]
		out_data.append((num,name))
	#print(out_data)
	db = connect_db()
	cursor = db.cursor()
	sql = "INSERT INTO champs (champId, name) VALUES (%s, %s)"
	cursor.executemany(sql, out_data)
	db.commit()
	return

def update_spells():
	return

def update_items():
	return

def update_runes():
	return

def patch():
	update_champions()
	update_spells()
	update_items()
	update_runes()
	return

update_champions()