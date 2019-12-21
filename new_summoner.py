from googleAPI import get_summoner_list, add_summoner_sheet
from riot import get_summoner
from pprint import pprint


def swap_names_ids(name_dicts):
	sum_list = get_summoner_list() 
	for side in name_dicts:
		for key in side:
			if side[key] in sum_list:
				side[key] = sum_list[side[key]]
			else:
				temp_id = get_summoner(side[key])
				add_summoner_sheet(side[key], temp_id)
				side[key] = temp_id
	return name_dicts