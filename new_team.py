from googleAPI import get_team_list, add_team_sheet
from pprint import pprint

def swap_team_ids(name, client):
	team_list = get_team_list(client)
	if name in team_list:
		return int(team_list[name])
	return add_team_sheet(client, name)