from googleAPI import get_inputs
from new_summoner import swap_names_ids
from new_team import swap_team_ids
from pprint import pprint

def main():
	in_data = get_inputs()
	in_data[0] = swap_team_ids(in_data[0])
	in_data[1] = swap_team_ids(in_data[1]) 
	in_data[2] = swap_names_ids(in_data[2])
	return in_data

pprint(main())