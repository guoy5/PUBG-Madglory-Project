# import packages
import json
import requests
import datetime
from .participant_object import *
from .telemetry_event import *
from .rank_system import *
from .match_object import *
from .player_object import *
from .result_object import *
from .score_calculation import *

# remember current time
current_time = datetime.datetime.now()

# urls and headers will be passed in using requests.get
URL = "https://api.pubg.com/shards/steam"
headers = {
  # replace [] with your own pubg api key
  "Authorization": "Bearer []",
  "Accept": "application/vnd.api+json"
}


def player_stats(playername):
	"""
	make api requests and aggregate stat here

	: type playername: string
	: rtype result: dictionary
	"""

	# ============   make an api request for player object  ==============
	url = URL + "/players?filter[playerNames]=" + playername
	r = requests.get(url, headers = headers)
	# if the connection fails, exit the function
	if (r.status_code != 200):
		return None
	# convert data into dictionary
	data = json.loads(r.text)
	# ===================================================================

	# create a new player object
	player = player_obj(data)

	# create three new result objects which are used to record the player performance under each game mode
	solo_stats, duo_stats, squad_stats = result_obj(), result_obj(), result_obj()

	# go through each match to retrive data we need
	for match_id in player.match_list:

		if (match_id['type'] == "match"):

			# ============   make an api request for match object  ==============
			url = URL + "/matches/{}".format(match_id['id'])
			one_match_r = requests.get(url, headers = headers)
			# if the connection fails, exit the function
			if (one_match_r.status_code != 200):
				return None
			# convert data into dictionary
			one_match_data = json.loads(one_match_r.text)
			# ===================================================================

			# create a match object
			match = match_obj(one_match_data)

			# only retrive data from recent 7 days matches
			if (current_time - match.createdAt).days > 7:
				break

			# extract the telemetry url and participant stats from match included array
			for i in match.included:
				if i['type'] == "asset" and i['id'] == match.asset_id:
					match.telemetry_url = i['attributes']['URL']
				if i['type'] == 'participant' and i['attributes']['stats']['playerId'] == player.id:
					participant_stats = i['attributes']['stats']
					participant = participant_obj(participant_stats)

			# retrive data we want from telemetry object
			weapon, pickups, pickupsfromcarepackages = extract_data_from_telemetry(match.telemetry_url, player.id)

			# calculate survival score and supply score for each match
			survival_score_ = survival_score(participant.timeSurvived, match.duration, participant.winPlace)
			supply_score_ = supply_score(pickups, pickupsfromcarepackages)

			# aggreate data
			gamemode = match.gameMode
			if gamemode == "solo" or gamemode == "solo-fpp" or gamemode == "normal-solo" or gamemode == "normal-solo-fpp":
				solo_stats.aggregate(participant, survival_score_, supply_score_, weapon)
			elif gamemode == "duo" or gamemode == "duo-fpp" or gamemode == "normal-duo" or gamemode == "normal-duo-fpp":
				duo_stats.aggregate(participant, survival_score_, supply_score_, weapon)
			else:
				squad_stats.aggregate(participant, survival_score_, supply_score_, weapon)

	# create three new rank objects to record the player's rank of each game mode
	solo_rank = create_rank(solo_stats)
	duo_rank = create_rank(duo_stats)
	squad_rank = create_rank(squad_stats)

	# Get overall results of each game mode
	solo_result = result_stats(solo_stats, solo_rank, "1")
	duo_result = result_stats(duo_stats, duo_rank, "2")
	squad_result = result_stats(squad_stats, squad_rank, "3")

	# combine these three results into one dictionary
	result = solo_result.copy()
	result.update(duo_result)
	result.update(squad_result)

	return result


def create_rank(stats):
	"""
	create the rank object to record player's performance and the final rank letter
	: type stats: result_obj
	: rtype rank: rank_obj
	"""
	rank = rank_obj()
	if stats.TotalGameCount > 0:
		rank.damage_score = damage_score(stats.AverageDamageDealt)
		rank.kill_score = kill_score(stats.AverageKills)
		rank.distance_score = distance_score(stats.AverageWalkDistance)
		rank.supply_score = stats.AverageSupplyScore
		rank.survival_score = stats.AverageSurvivalScore
		rank.final_rank()
	return rank



def result_stats(stats, rank, gamemode):

	"""
	store all stats which need to be shown in the front-end in a dictionary
	structure to make them easier to pass to the front-end

	: type stats: result_obj
	: type most_used_weapon: list
	: type rank: rank_obj
	: type gamemode: string
	: rtype result: dictionary
	"""

	result = {}
	result["TotalAssists" + gamemode] = stats.TotalAssists
	result["LongestRangeKill" + gamemode] = format(stats.LongestKill, '.2f')
	result["TotalHeadshots" + gamemode] = stats.TotalHeadshots
	result["WinRatio" + gamemode] = format(stats.WinRatio, '.2f')
	result["TotalWinLosses" + gamemode] = (stats.TotalWins, stats.TotalLosses)
	result["TotalKills" + gamemode] = stats.TotalKills
	result["AvgKills" + gamemode] = format(stats.AverageKills, '.2f')
	result["numberofsuicides" + gamemode] = stats.TotalSuicides
	result["numberofteamkills" + gamemode] = stats.TotalTeamkills
	result["Avgdamagematch" + gamemode] = format(stats.AverageDamageDealt, '.2f')
	result["Avgfinishplace" + gamemode] = int(stats.AverageWinPlace)
	result["TotalRevives" + gamemode] = stats.TotalRevives
	result["MostUsedWeapon" + gamemode] = stats.MostUsedWeapon
	result['final_score' + gamemode] = rank.final_score
	result['damage_score' + gamemode] = rank.damage_score
	result['kill_score' + gamemode] = rank.kill_score
	result['survival_score' + gamemode] = rank.survival_score
	result['supply_score' + gamemode] = rank.supply_score
	result['distance_score' + gamemode] = rank.distance_score
	result['TotalGameCount' + gamemode] = stats.TotalGameCount
	result['TotalWins' + gamemode] = stats.TotalWins
	result['TotalLosses' + gamemode] = stats.TotalLosses

	return result
