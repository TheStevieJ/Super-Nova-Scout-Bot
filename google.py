import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

def package(list):
	temp = []
	temp.append(list[0])
	temp.append(list[1])
	rosters = [{},{}]
	mod = 0
	for team in rosters:
		team["TOP"] = list[2 + mod]
		team["JNG"] = list[3 + mod]
		team["MID"] = list[4 + mod]
		team["ADC"] = list[5 + mod]
		team["SUP"] = list[6 + mod]
		mod = 1
	temp.append(rosters)
	picks = [[],[]]
	mod = 12
	for side in picks:
		for x in range(0,5):
			side.append(list[mod + x])
		mod = 17
	temp.append(picks)
	temp.append(list[22])
	bans = [[],[]]
	if list[23] == 'Yes':
		mod = 24
		for side in bans:
			for x in range(0,5):
				side.append(list[mod + x])
			mod = 29
	temp.append(bans)
	return temp


def reduce_history_url(url):
	return url.split("/")[-2]


def get_inputs():
	scope = ['https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
	creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
	client = gspread.authorize(creds)
	sheet = client.open("SNInfo")
	worksheet = sheet.get_worksheet(2)
	col = worksheet.col_values(1)
	col[22] = reduce_history_url(col[22])
	return col


pprint(package(get_inputs()))