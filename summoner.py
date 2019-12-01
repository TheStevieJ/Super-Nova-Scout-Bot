import mysql.connector
from request import api_request
from database import connect_db

summoner_list = {}


def new_summoner(name):
	r_name = name.replace(" ","%20")
	url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + r_name + "?"
	data = api_request(url)
	accId = data["accountId"]
	upload_summoner(name, accId)
	summoner_list[name] = accId
	return accId


def get_summoner_id(name):
	if name in summoner_list.keys():
		return summoner_list[name]
	return new_summoner(name)


def upload_summoner(name, accId):
	db = connect_db()
	cursor = db.cursor()
	sql = "INSERT INTO players(accountId, name) VALUES (%s, %s)"
	val = (accId, name)
	cursor.execute(sql, val)
	db.commit()
	return True


def get_summoner_list():
	db = connect_db()
	cursor = db.cursor()
	cursor.execute("SELECT name, accountId FROM players")
	data = cursor.fetchall()
	for player in data:
		summoner_list[player[0]] = player[1]
	return True