import gspread
import sys
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

def establish_creds():
	scope = ['https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
	creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
	client = gspread.authorize(creds)
	return client

def package(list):
	temp = []
	#Team Names
	temp.append(list[0])
	temp.append(list[1])
	#Rosters
	rosters = [{},{}]
	start_index = 2
	booster = 0
	for side in rosters:
		side[0] = list[start_index + booster]
		side[1] = list[start_index + 1 + booster]
		side[2] = list[start_index + 2 + booster]
		side[3] = list[start_index + 3 + booster]
		side[4] = list[start_index + 4 + booster]
		booster = 5
	temp.append(rosters)
	#Picks
	picks = [[],[]]
	start_index = 12
	booster = 0
	for side in picks:
		for x in range(0,5):
			side.append((list[x*2 + start_index + booster],list[x*2 + start_index + booster + 1]))
		booster = 10
	temp.append(picks)
	#Match Id
	temp.append(reduce_history_url(list[32]))
	#Bans
	bans = [[],[]]
	if list[33] == "Yes":
		start_index = 34
		booster = 0
		for side in bans:
			for x in range(0,5):
				side.append(list[x + start_index + booster])
			booster = 5
	temp.append(bans)
	return temp


def reduce_history_url(url):
	return url.split("/")[-2]


def get_inputs(client):
	sheet = client.open("SNInfo")
	worksheet = sheet.worksheet("Output")
	col = worksheet.col_values(1)
	return package(col)


def get_summoner_list(client):
	sheet = client.open("SNInfo")
	worksheet = sheet.worksheet("PlayerDB")
	names = worksheet.col_values(1)
	ids = worksheet.col_values(2)
	end_dict = {}
	for x in range(0,len(names)):
		end_dict[names[x]] = ids[x]
	return end_dict


def add_summoner_sheet(client, name, id):
	sheet = client.open("SNInfo")
	worksheet = sheet.worksheet("PlayerDB")
	row = [name, id]
	worksheet.insert_row(row,1)
	return


def get_team_list(client):
	sheet = client.open("SNInfo")
	worksheet = sheet.worksheet("TeamDB")
	names = worksheet.col_values(1)
	ids = worksheet.col_values(2)
	end_dict = {}
	for x in range(0,len(names)):
		end_dict[names[x]] = ids[x]
	return end_dict


def add_team_sheet(client, name):
	sheet = client.open("SNInfo")
	worksheet = sheet.worksheet("TeamDB")
	last_id = worksheet.cell(1,2).value
	if last_id is "":
		last_id = 0
	row = [name, int(last_id) + 1]
	worksheet.insert_row(row,1)
	return int(last_id) + 1


def get_match_list(client, id):
	sheet = client.open("SNInfo")
	worksheet = sheet.worksheet("RawMatch")
	matches = worksheet.col_values(1)
	return str(id) in matches


def add_match(client, game_info, blue_id, red_id):
	if get_match_list(client, game_info["gameId"]) is True:
		sys.exit("Match " + str(game_info["gameId"]) + " already exisists in sheet")
	sheet = client.open("SNInfo")
	worksheet = sheet.worksheet("RawMatch")
	row = [
		game_info["gameId"],
		blue_id,
		red_id,
		game_info["platformId"],
		game_info["gameCreation"],
		game_info["gameDuration"],
		game_info["queueId"],
		game_info["mapId"],
		game_info["seasonId"],
		game_info["gameVersion"],
		game_info["gameMode"],
		game_info["gameType"]
	]
	worksheet.insert_row(row,2)
	return game_info["gameId"]


def add_data(client, data, sheet_name):
	sheet = client.open("SNInfo")
	#worksheet = sheet.worksheet(sheet_name)
	sheet.values_append(
		sheet_name + '!A2',
		params={'valueInputOption':'RAW'},
		body={'values': data}
	)
	return

