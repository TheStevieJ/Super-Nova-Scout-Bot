from googleAPI import get_team_list, add_team_sheet
from pprint import pprint

def swap_team_ids(name):
	team_list = get_team_list()
	if name in team_list:
		return team_list[name]
	return add_team_sheet(name)