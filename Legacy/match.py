import requests
import mysql.connector
import time
from datetime import datetime, timezone
from database import connect_db
from summoner import get_summoner_id
from request import load_key
API_KEY = load_key()

def riot_api_call(matchId):
	url = "https://na1.api.riotgames.com/lol/match/v4/matches/"+ matchId + "?api_key=" + API_KEY
	r = requests.get(url,{})
	data = r.json()
	return data

def team_side(number):
	if number is 100:
		return "blue"
	return "red"

def package_data(data, blueId, redId, bluePlayerIds, redPlayerIds, blueDraft, redDraft):
	#Match Info
	#print(data)
	match_info = {}
	match_info["season"] = data["seasonId"]
	match_info["gameId"] = data["gameId"]
	match_info["patch"] = data["gameVersion"]
	match_info["duration"] = data["gameDuration"]
	match_info["creation"] = data["gameCreation"]
	#Team Stats
	team_stats = []
	pick_bans = []
	team_ids = {
		100 : blueId,
		200 : redId
	}
	for team_data in data["teams"]:
		temp_data = {}
		temp_data["gameId"] = str(data["gameId"])
		temp_data["teamId"] = team_ids[team_data["teamId"]]
		temp_data["side"] = team_side(team_data["teamId"])
		temp_data["firstDrag"] = team_data["firstDragon"]
		temp_data["firstInhib"] = team_data["firstInhibitor"]
		temp_data["barons"] = team_data["baronKills"]
		temp_data["firstHerald"] = team_data["firstRiftHerald"]
		temp_data["firstBaron"] = team_data["firstBaron"]
		temp_data["heralds"] = team_data["riftHeraldKills"]
		temp_data["firstBlood"] = team_data["firstBlood"]
		temp_data["firstTower"] = team_data["firstTower"]
		temp_data["inhibs"] = team_data["inhibitorKills"]
		temp_data["towers"] = team_data["towerKills"]
		temp_data["win"] = team_data["win"]
		temp_data["drags"] = team_data["dragonKills"]
		team_stats.append(temp_data)
		#Pick Ban
		for x in range(0, len(team_data["bans"])):
			temp_ban = {}
			ban_data = team_data["bans"][x]
			temp_ban["gameId"] = str(data["gameId"])
			temp_ban["side"] = temp_data["side"]
			temp_ban["pickNum"] = (x + 1)
			temp_ban["champion"] = ban_data["championId"]
			temp_ban["ban"] = True
			pick_bans.append(temp_ban)
	for x in range(0, len(blueDraft)):
		temp_ban = {}
		temp_ban["gameId"] = str(data["gameId"])
		temp_ban["side"] = "blue"
		temp_ban["pickNum"] = (x + 1)
		temp_ban["champion"] = blueDraft[x]
		temp_ban["ban"] = False
		pick_bans.append(temp_ban)
	for x in range(0, len(redDraft)):
		temp_ban = {}
		temp_ban["gameId"] = str(data["gameId"])
		temp_ban["side"] = "red"
		temp_ban["pickNum"] = (x + 1)
		temp_ban["champion"] = redDraft[x]
		temp_ban["ban"] = False
		pick_bans.append(temp_ban)

	#Player Stats
	player_stats = []
	player_timelines = []
	player_ids = {
		100 : {
			"TOP": { "SOLO": bluePlayerIds["TOP"]},
			"JUNGLE": { "NONE": bluePlayerIds["JNG"]},
			"MIDDLE": { 
				"SOLO": bluePlayerIds["MID"],
				"DUO_CARRY": bluePlayerIds["MID"]
			},
			"BOTTOM" : {
				"DUO_CARRY": bluePlayerIds["ADC"],
				"DUO_SUPPORT": bluePlayerIds["SUP"]
			}
		},
		200: {
			"TOP": { "SOLO": redPlayerIds["TOP"]},
			"JUNGLE": { "NONE": redPlayerIds["JNG"]},
			"MIDDLE": { 
				"SOLO": redPlayerIds["MID"],
				"DUO_CARRY": redPlayerIds["MID"]
			},
			"BOTTOM" : {
				"DUO_CARRY": redPlayerIds["ADC"],
				"DUO_SUPPORT": redPlayerIds["SUP"]
			}
		}
	}
	for player_data in data["participants"]:
		temp_data = {}
		temp_data["gameId"] = str(data["gameId"])
		temp_data["side"] = team_side(player_data["teamId"])
		temp_data["parId"] = player_data["participantId"]
		temp_data["spell1"] = player_data["spell1Id"]
		temp_data["spell2"] = player_data["spell2Id"]
		temp_data["champion"] = player_data["championId"]
		temp_stats = player_data["stats"]
		temp_data["firstBloodKill"] = temp_stats["firstBloodKill"]
		temp_data["firstBloodAsst"] = temp_stats["firstBloodAssist"]
		temp_data["visionScore"] = temp_stats["visionScore"]
		temp_data["wardsPlaced"] = temp_stats["wardsPlaced"]
		temp_data["visionWards"] = temp_stats["visionWardsBoughtInGame"]
		temp_data["sightWards"] = temp_stats["sightWardsBoughtInGame"]
		temp_data["wardsKilled"] = temp_stats["wardsKilled"]
		temp_data["kills"] = temp_stats["kills"]
		temp_data["deaths"] = temp_stats["deaths"]
		temp_data["assists"] = temp_stats["assists"]
		temp_data["physicalToChamps"] = temp_stats["physicalDamageDealtToChampions"]
		temp_data["magicToChamps"] = temp_stats["magicDamageDealtToChampions"]
		temp_data["trueToChamps"] = temp_stats["trueDamageDealtToChampions"]
		temp_data["totalToChamps"] = temp_stats["totalDamageDealtToChampions"]
		temp_data["goldEarned"] = temp_stats["goldEarned"]
		temp_data["goldSpent"] = temp_stats["goldSpent"]
		temp_data["inhibs"] = temp_stats["inhibitorKills"]
		temp_data["damageToObjectives"] = temp_stats["damageDealtToObjectives"]
		temp_data["damageToTowers"] = temp_stats["damageDealtToTurrets"]
		temp_data["towers"] = temp_stats["turretKills"]
		temp_data["largestKillSpree"] = temp_stats["largestKillingSpree"]
		temp_data["totalMinions"] = temp_stats["totalMinionsKilled"]
		temp_data["enemyJungleMinions"] = temp_stats["neutralMinionsKilledEnemyJungle"]
		temp_data["ownJungleMinions"] = temp_stats["neutralMinionsKilledTeamJungle"]
		temp_data["level"] = temp_stats["champLevel"]
		temp_data["perk0"] = temp_stats["perk0"]
		temp_data["perk1"] = temp_stats["perk1"]
		temp_data["perk2"] = temp_stats["perk2"]
		temp_data["perk3"] = temp_stats["perk3"]
		temp_data["perk4"] = temp_stats["perk4"]
		temp_data["perk5"] = temp_stats["perk5"]
		temp_data["item0"] = temp_stats["item0"]
		temp_data["item1"] = temp_stats["item1"]
		temp_data["item2"] = temp_stats["item2"]
		temp_data["item3"] = temp_stats["item3"]
		temp_data["item4"] = temp_stats["item4"]
		temp_data["item5"] = temp_stats["item5"]
		temp_data["item6"] = temp_stats["item6"]
		timeline_data = player_data["timeline"]
		temp_data["role"] = timeline_data["role"]
		temp_data["lane"] = timeline_data["lane"]
		temp_data["teamId"] = team_ids[player_data["teamId"]]
		print(temp_data["lane"],temp_data["role"])
		temp_data["accountId"] = player_ids[player_data["teamId"]][temp_data["lane"]][temp_data["role"]]
		player_stats.append(temp_data)
		#Player Timelines
		print(timeline_data)
		for x in range(0, len(timeline_data["creepsPerMinDeltas"])):
			temp_timeline = {}
			temp_timeline["gameId"] = str(data["gameId"])
			temp_timeline["parId"] = temp_data["parId"]
			times = list(timeline_data["creepsPerMinDeltas"].keys())
			my_time = times[x]
			temp_timeline["time"] = my_time
			temp_timeline["csDelta"] = timeline_data["creepsPerMinDeltas"][my_time]
			temp_timeline["xpDelta"] = timeline_data["xpPerMinDeltas"][my_time]
			temp_timeline["goldDelta"] = timeline_data["goldPerMinDeltas"][my_time]
			temp_timeline["csDiffDelta"] = timeline_data["csDiffPerMinDeltas"][my_time]
			temp_timeline["xpDiffDelta"] = timeline_data["xpDiffPerMinDeltas"][my_time]
			temp_timeline["dmgTakenDelta"] = timeline_data["damageTakenPerMinDeltas"][my_time]
			temp_timeline["dmgTakenDiffDelta"] = timeline_data["damageTakenDiffPerMinDeltas"][my_time]
			player_timelines.append(temp_timeline)
	match_data = {
		"match_info": match_info,
		"team_stats": team_stats,
		"pick_bans": pick_bans,
		"player_stats": player_stats,
		"player_timelines": player_timelines
	}
	return match_data

def send_data(data):
	db = connect_db()
	cursor = db.cursor()
	#Match Info
	sql = "INSERT INTO match_info (gameId, season, patch, duration, creation) VALUES (%s, %s, %s, %s, %s)"
	match_data = data["match_info"]
	val = (
		match_data["gameId"],
		match_data["season"],
		match_data["patch"],
		match_data["duration"],
		time.gmtime(match_data["creation"]/1000)
		)
	cursor.execute(sql, val)
	#Team Stats
	sql = "INSERT INTO team_stats (gameId, teamId, side, firstDrag, firstInhib, barons, firstHerald, firstBaron, heralds, firstBlood, firstTower, inhibs, towers, win, drags) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
	val = []
	for team in data["team_stats"]:
		temp = (
			team["gameId"],
			team["teamId"],
			team["side"],
			team["firstDrag"],
			team["firstInhib"],
			team["barons"],
			team["firstHerald"],
			team["firstBaron"],
			team["heralds"],
			team["firstBlood"],
			team["firstTower"],
			team["inhibs"],
			team["towers"],
			team["win"],
			team["drags"]
			)
		val.append(temp)
	cursor.executemany(sql,val)
	#Player Stats
	sql = "INSERT INTO player_stats (gameId, side, parId, spell1, spell2, champion, firstBloodKill, firstBloodAsst, visionScore, wardsPlaced, visionWards, sightWards, wardsKilled, kills, deaths, assists, physicalToChamps, magicToChamps, trueToChamps, totalToChamps, goldEarned, goldSpent, inhibs, damageToObjectives, damageToTowers, towers, largestKillSpree, laneMinions, enemyJungleMinions, ownJungleMinions, level, perk0, perk1, perk2, perk3, perk4, perk5, item0, item1, item2, item3, item4, item5, item6, role, lane, teamId, accountId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
	val = []
	for player in data["player_stats"]:
		temp = (
			player["gameId"],
			player["side"],
			player["parId"],
			player["spell1"],
			player["spell2"],
			player["champion"],
			player["firstBloodKill"],
			player["firstBloodAsst"],
			player["visionScore"],
			player["wardsPlaced"],
			player["visionWards"],
			player["sightWards"],
			player["wardsKilled"],
			player["kills"],
			player["deaths"],
			player["assists"],
			player["physicalToChamps"],
			player["magicToChamps"],
			player["trueToChamps"],
			player["totalToChamps"],
			player["goldEarned"],
			player["goldSpent"],
			player["inhibs"],
			player["damageToObjectives"],
			player["damageToTowers"],
			player["towers"],
			player["largestKillSpree"],
			player["totalMinions"],
			player["enemyJungleMinions"],
			player["ownJungleMinions"],
			player["level"],
			player["perk0"],
			player["perk1"],
			player["perk2"],
			player["perk3"],
			player["perk4"],
			player["perk5"],
			player["item0"],
			player["item1"],
			player["item2"],
			player["item3"],
			player["item4"],
			player["item5"],
			player["item6"],
			player["role"],
			player["lane"],
			player["teamId"],
			player["accountId"]
			)
		val.append(temp)
	cursor.executemany(sql,val)
	#Pick Bans
	sql = "INSERT INTO pick_bans(gameId, side, pickNum, champion, ban) VALUES (%s, %s, %s, %s, %s)"
	val = []
	for pick in data["pick_bans"]:
		temp = (
			pick["gameId"],
			pick["side"],
			pick["pickNum"],
			pick["champion"],
			pick["ban"]
			)
		val.append(temp)
	cursor.executemany(sql,val)
	#Player Timelines
	sql = "INSERT INTO player_timelines(gameId, parId, time, csDelta, xpDelta, goldDelta, csDiffDelta, xpDiffDelta, dmgTakenDelta, dmgTakenDiffDelta) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
	val = []
	for seg in data["player_timelines"]:
		temp = (
			seg["gameId"],
			seg["parId"],
			seg["time"],
			seg["csDelta"],
			seg["xpDelta"],
			seg["goldDelta"],
			seg["csDiffDelta"],
			seg["xpDiffDelta"],
			seg["dmgTakenDelta"],
			seg["dmgTakenDiffDelta"]
			)
		val.append(temp)
	cursor.executemany(sql,val)
	db.commit()
	return

def repack_summoners(team_list):
	team_list["TOP"] = get_summoner_id(team_list["TOP"])
	team_list["JNG"] = get_summoner_id(team_list["JNG"])
	team_list["MID"] = get_summoner_id(team_list["MID"])
	team_list["ADC"] = get_summoner_id(team_list["ADC"])
	team_list["SUP"] = get_summoner_id(team_list["SUP"])
	#print (team_list)
	return team_list

def main(team1, team2, blueNames, redNames, blueDraft, redDraft, matchId):
	raw_data = riot_api_call(matchId)
	print("pass")
	formated_data = package_data(raw_data, team1, team2, repack_summoners(blueNames), repack_summoners(redNames), blueDraft, redDraft)
	print("pass2")
	send_data(formated_data)
	print("fullpass")
	return
"""
blue = {
	"TOP": 'blueTop',
	"JNG": 'blueJng',
	"MID": 'blueMid',
	"ADC": 'blueAdc',
	"SUP": 'blueSup'
}
red = {
	"TOP": 'redTop',
	"JNG": 'redJng',
	"MID": 'redMid',
	"ADC": 'redAdc',
	"SUP": 'redSup'
}
blueDraft = [1,2,3,4,5]
redDraft = [6,7,8,9,0]
main("team1", "team2", blue, red, blueDraft, redDraft, "3216654209")
"""