import mysql.connector
from request import api_request
from database import connect_db

team_list = {}


def new_team(name):
	db = connect_db()
	cursor = db.cursor()
	sql = "INSERT INTO teams(name) VALUES (%s)"
	val = (name,)
	cursor.execute(sql,val)
	db.commit()
	return cursor.lastrowid

def get_team_id(name):
	if name in team_list.keys():
		return team_list[name]
	return new_team(name)

def get_team_list():
	db = connect_db()
	cursor = db.cursor()
	cursor.execute("SELECT name, teamId FROM teams")
	data = cursor.fetchall()
	for team in data:
		team_list[team[0]] = team[1]
	return True

get_team_list()
print(get_team_id("Radiance"))