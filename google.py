import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint


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
	pprint(temp)
	return temp


def reduce_history_url(url):
	return url.split("/")[-2]


def get_inputs():
	scope = ['https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
	creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
	client = gspread.authorize(creds)
	sheet = client.open("SNInfo")
	worksheet = sheet.worksheet("Output")
	col = worksheet.col_values(1)
	#col[22] = reduce_history_url(col[22])
	return col

def get_summoner_list():
	scope = ['https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
	creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
	client = gspread.authorize(creds)
	sheet = client.open("SNInfo")
	worksheet = sheet.worksheet("PlayerDB")
	names = worksheet.col_values(1)
	ids = worksheet.col_values(2)
	end_dict = {}
	for x in range(0,len(names)):
		end_dict[names[x]] = ids[x]
	return end_dict

pprint(get_summoner_list())