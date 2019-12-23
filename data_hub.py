from googleAPI import add_match, add_team_data, add_player_data, add_time_data, add_pick_ban_data
from pprint import pprint

def build_player_champ_dict(in_data):
	player_champ = {}
	for x in range(0,2):
		for champ in in_data[3][x]:
			player_champ[champ[0]] = (in_data[2][x][int(champ[1])], champ[1])
	return player_champ

def format_pick_info(in_data, match_data):
	picks1 = [
		(in_data[0], in_data[3][0][0][0], 100, 1, "False"),
		(in_data[1], in_data[3][1][0][0], 200, 1, "False"),
		(in_data[1], in_data[3][1][1][0], 200, 2, "False"),
		(in_data[0], in_data[3][0][1][0], 100, 2, "False"),
		(in_data[0], in_data[3][0][2][0], 100, 3, "False"),
		(in_data[1], in_data[3][1][2][0], 200, 3, "False")
	]
	picks2 = [
		(in_data[1], in_data[3][1][3][0], 200, 4, "False"),
		(in_data[0], in_data[3][0][3][0], 100, 4, "False"),
		(in_data[0], in_data[3][0][4][0], 100, 5, "False"),
		(in_data[1], in_data[3][0][4][0], 200, 5, "False")
	]

	bans1 = []
	bans2 = []
	if not in_data[5][0]:	
		for x in range(0,3):
			for y in range(0,2):
				bans1.append((in_data[y], match_data["teams"][y]["bans"][x]["championId"], match_data["teams"][y]["teamId"], x + 1, "True"))
		for x in range(3,5):
			for y in range(0,2):
				bans2.append((in_data[y], match_data["teams"][y]["bans"][x]["championId"], match_data["teams"][y]["teamId"], x + 1, "True"))
	else:
		for x in range(0,3):
			for y in range(0,2):
				bans1.append((in_data[y], in_data[5][y][x], (y + 1) * 100, x + 1, "True"))
		for x in range(3,5):
			for y in range(0,2):
				bans2.append((in_data[y], in_data[5][y][x], (y + 1) * 100, x + 1, "True"))

	return bans1+picks1+bans2+picks2

def parse_data(in_data, match_data, client):
	match_id = in_data[4]
	add_match(client, match_data, in_data[0], in_data[1])
	for team in match_data["teams"]:
		team_id = in_data[int(team["teamId"] / 100) - 1]
		add_team_data(match_id, client, team, team_id)
	player_champ = build_player_champ_dict(in_data)
	for player in match_data["participants"]:
		player_id, role = player_champ[str(player["championId"])]
		add_player_data(match_id, client, player, player_id, role)
		time = player["timeline"]
		for x in range(0, len(time["xpPerMinDeltas"])):
			first = x * 10
			second = (x * 10) + 10
			time_name = str(first) + "-" + str(second)
			time_info = [
				time["creepsPerMinDeltas"][time_name],
				time["xpPerMinDeltas"][time_name],
				time["goldPerMinDeltas"][time_name],
				time["damageTakenPerMinDeltas"][time_name]
			]
			name = time_name.split("-")
			add_time_data(match_id, player_id, client, time_info, name[1])
	pick_ban_data = format_pick_info(in_data, match_data)
	for x in range(len(pick_ban_data)):
		add_pick_ban_data(match_id, client, pick_ban_data[x], x+1)
	return
