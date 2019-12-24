from googleAPI import add_match, add_data
from pprint import pprint


def build_player_champ_dict(in_data):
	player_champ = {}
	for x in range(0,2):
		for champ in in_data[3][x]:
			player_champ[champ[0]] = (in_data[2][x][int(champ[1])], champ[1])
	return player_champ


def format_pick_info(in_data, match_data):
	picks1 = [
		(int(in_data[0]), int(in_data[3][0][0][0]), 100, 1, "FALSE"),
		(int(in_data[1]), int(in_data[3][1][0][0]), 200, 1, "FALSE"),
		(int(in_data[1]), int(in_data[3][1][1][0]), 200, 2, "FALSE"),
		(int(in_data[0]), int(in_data[3][0][1][0]), 100, 2, "FALSE"),
		(int(in_data[0]), int(in_data[3][0][2][0]), 100, 3, "FALSE"),
		(int(in_data[1]), int(in_data[3][1][2][0]), 200, 3, "FALSE")
	]
	picks2 = [
		(int(in_data[1]), int(in_data[3][1][3][0]), 200, 4, "FALSE"),
		(int(in_data[0]), int(in_data[3][0][3][0]), 100, 4, "FALSE"),
		(int(in_data[0]), int(in_data[3][0][4][0]), 100, 5, "FALSE"),
		(int(in_data[1]), int(in_data[3][1][4][0]), 200, 5, "FALSE")
	]

	bans1 = []
	bans2 = []
	if not in_data[5][0]:	
		for x in range(0,3):
			for y in range(0,2):
				bans1.append((int(in_data[y]), match_data["teams"][y]["bans"][x]["championId"], match_data["teams"][y]["teamId"], x + 1, "TRUE"))
		for x in range(3,5):
			for y in range(0,2):
				bans2.append((int(in_data[y]), match_data["teams"][y]["bans"][x]["championId"], match_data["teams"][y]["teamId"], x + 1, "TRUE"))
	else:
		for x in range(0,3):
			for y in range(0,2):
				bans1.append((int(in_data[y]), in_data[5][y][x], (y + 1) * 100, x + 1, "TRUE"))
		for x in range(3,5):
			for y in range(0,2):
				bans2.append((int(in_data[y]), in_data[5][y][x], (y + 1) * 100, x + 1, "TRUE"))

	return bans1+picks1+bans2+picks2


def make_team_data(match_id, team_info, team_id):
	row = [
		match_id,
		team_info["teamId"],
		team_id,
		team_info["win"],
		team_info["firstBlood"],
		team_info["firstTower"],
		team_info["firstInhibitor"],
		team_info["firstBaron"],
		team_info["firstDragon"],
		team_info["firstRiftHerald"],
		team_info["towerKills"],
		team_info["inhibitorKills"],
		team_info["baronKills"],
		team_info["dragonKills"],
		team_info["riftHeraldKills"]
	]
	return row


def make_player_data(match_id, player_info, player_id, role):
	stats = player_info["stats"]
	row = [
		match_id,
		player_id,
		player_info["teamId"],
		int(role),
		player_info["championId"],
		player_info["spell1Id"],
		player_info["spell2Id"],
		stats["item0"],
		stats["item1"],
		stats["item2"],
		stats["item3"],
		stats["item4"],
		stats["item5"],
		stats["item6"],
		stats["kills"],
		stats["deaths"],
		stats["assists"],
		stats["largestKillingSpree"],
		stats["largestMultiKill"],
		stats["longestTimeSpentLiving"],
		stats["doubleKills"],
		stats["tripleKills"],
		stats["quadraKills"],
		stats["pentaKills"],
		stats["totalDamageDealt"],
		stats["magicDamageDealt"],
		stats["physicalDamageDealt"],
		stats["trueDamageDealt"],
		stats["largestCriticalStrike"],
		stats["totalDamageDealtToChampions"],
		stats["magicDamageDealtToChampions"],
		stats["physicalDamageDealtToChampions"],
		stats["trueDamageDealtToChampions"],
		stats["totalHeal"],
		stats["totalUnitsHealed"],
		stats["damageSelfMitigated"],
		stats["damageDealtToObjectives"],
		stats["damageDealtToTurrets"],
		stats["visionScore"],
		stats["timeCCingOthers"],
		stats["totalDamageTaken"],
		stats["magicalDamageTaken"],
		stats["physicalDamageTaken"],
		stats["trueDamageTaken"],
		stats["goldEarned"],
		stats["goldSpent"],
		stats["turretKills"],
		stats["inhibitorKills"],
		stats["totalMinionsKilled"],
		stats["neutralMinionsKilled"],
		stats["neutralMinionsKilledTeamJungle"],
		stats["neutralMinionsKilledEnemyJungle"],
		stats["totalTimeCrowdControlDealt"],
		stats["champLevel"],
		stats["visionWardsBoughtInGame"],
		stats["sightWardsBoughtInGame"],
		stats["wardsPlaced"],
		stats["wardsKilled"],
		stats["firstBloodKill"],
		stats["firstBloodAssist"],
		stats["firstTowerKill"],
		stats["firstTowerAssist"],
		stats["firstInhibitorKill"],
		stats["firstInhibitorAssist"],
		stats["perk0"],
		stats["perk0Var1"],
		stats["perk0Var2"],
		stats["perk0Var3"],
		stats["perk1"],
		stats["perk1Var1"],
		stats["perk1Var2"],
		stats["perk1Var3"],
		stats["perk2"],
		stats["perk2Var1"],
		stats["perk2Var2"],
		stats["perk2Var3"],
		stats["perk3"],
		stats["perk3Var1"],
		stats["perk3Var2"],
		stats["perk3Var3"],
		stats["perk4"],
		stats["perk4Var1"],
		stats["perk4Var2"],
		stats["perk4Var3"],
		stats["perk5"],
		stats["perk5Var1"],
		stats["perk5Var2"],
		stats["perk5Var3"],
		stats["perkPrimaryStyle"],
		stats["perkSubStyle"],
		stats["statPerk0"],
		stats["statPerk1"],
		stats["statPerk2"]
	]
	return row


def make_time_data(match_id, player_id, time_info, time):
	if time == 'end':
		time = -1
	row = [
		match_id,
		player_id,
		int(time),
		time_info[0],
		time_info[1],
		time_info[2],
		time_info[3]
	]
	return row


def make_pick_ban_data(match_id, pick_info, overall):
	row = [
		match_id,
		pick_info[0],
		pick_info[1],
		pick_info[2],
		pick_info[3],
		overall,
		pick_info[4]
	]
	return row


def parse_data(in_data, match_data, client):
	match_id = in_data[4]
	add_match(client, match_data, in_data[0], in_data[1])
	team_list = []
	for team in match_data["teams"]:
		team_id = in_data[int(team["teamId"] / 100) - 1]
		team_list.append(make_team_data(match_id, team, team_id))
	add_data(client, team_list, "RawTeam")
	player_champ = build_player_champ_dict(in_data)
	player_list = []
	time_list = []
	for player in match_data["participants"]:
		player_id, role = player_champ[str(player["championId"])]
		player_list.append(make_player_data(match_id, player, player_id, role))
		#TODO google sheets players
		time = player["timeline"]
		time_names = list(time["xpPerMinDeltas"].keys())
		for time_name in time_names:
			#first = x * 10
			#second = (x * 10) + 10
			#time_name = str(first) + "-" + str(second)
			time_info = [
				time["creepsPerMinDeltas"][time_name],
				time["xpPerMinDeltas"][time_name],
				time["goldPerMinDeltas"][time_name],
				time["damageTakenPerMinDeltas"][time_name]
			]
			name = time_name.split("-")
			time_list.append(make_time_data(match_id, player_id, time_info, name[1]))
	
	add_data(client, player_list, "RawPlayer")
	add_data(client, time_list, "RawTime")
	pick_ban_data = format_pick_info(in_data, match_data)
	pick_ban_list = []
	for x in range(len(pick_ban_data)):
		pick_ban_list.append(make_pick_ban_data(match_id, pick_ban_data[x], x+1))
	add_data(client, pick_ban_list, "RawPickBan")
	return