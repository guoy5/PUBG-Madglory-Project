import json
import requests

def extract_data_from_telemetry(url, player_id):
	"""
	We look for three telemetry events:
	LogPlayerAttack, LogItemPickup, LogItemPickupFromCarepackage

	: type url: string
	: type player_id: string
	: rtype weapon: string
	: rtype pickups: dict
	: rtype pickupsfromcarepackages: int
	"""

	# ============   make an api request for telemetry object  ==============
	r = requests.get(url, headers = {'Accept-Encoding': 'gzip'})
	# if the connection fails, exit the function
	if r.status_code != 200:
		return None, None, None
	# convert data into dictionary
	data = json.loads(r.text)
	# ===================================================================

	weapons = {}
	pickups = {}
	pickupsfromcarepackages = 0

	for i in data:
		# 1. Record every used weapons of a particular player in game
		if (i["_T"] == "LogPlayerAttack" and i["common"]["isGame"] > 0.5 and i["attackType"] == "Weapon" and i["attacker"]["accountId"] == player_id):
			weapons[i["weapon"]["itemId"]] = weapons.get(i["weapon"]["itemId"], 0) + 1

		# 2. Record every pickups of a particular player in game
		if (i["_T"] == "LogItemPickup" and i["common"]["isGame"] > 0.5 and i["character"]["accountId"] == player_id):
			pickups[i["item"]["category"]] = pickups.get(i["item"]["category"], 0) + 1

		# 3. Count how many care packages picked up by a particular player in game
		if (i["_T"] == "LogItemPickupFromCarepackage" and i["common"]["isGame"] > 0.5 and i["character"]["accountId"] == player_id):
			pickupsfromcarepackages += 1

		# find the most used weapon for each match
		if weapons != {}:
			weapon = max(weapons, key = weapons.get)
		else:
			weapon = None

	return weapon, pickups, pickupsfromcarepackages
