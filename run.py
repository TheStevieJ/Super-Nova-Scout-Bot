from googleAPI import get_inputs, establish_creds
from new_summoner import swap_names_ids
from new_team import swap_team_ids
from pprint import pprint
from riot import get_match
from data_hub import parse_data

def main():
	client = establish_creds()
	in_data = get_inputs(client)
	in_data[0] = swap_team_ids(in_data[0], client)
	in_data[1] = swap_team_ids(in_data[1], client) 
	in_data[2] = swap_names_ids(in_data[2], client)
	match_data = get_match(in_data[4])
	parse_data(in_data, match_data, client)
	return

main()