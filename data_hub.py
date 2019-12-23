from googleAPI import add_match, add_team_data
from pprint import pprint

def build_player_champ_dict(in_data):
	player_champ = {}
	for x in range(0,2):
		for champ in in_data[3][x]:
			player_champ[champ[0]] = in_data[2][x][int(champ[1])]
	return player_champ

def parse_data(in_data, match_data, client):
	id = add_match(client, match_data, in_data[0], in_data[1])
	for team in match_data["teams"]:
		team_id = in_data[int(team["teamId"] / 100) - 1]
		add_team_data(client, team, team_id)
	player_champ = build_player_champ_dict(in_data)
	#for player in match_data["particpants"]:


	return
