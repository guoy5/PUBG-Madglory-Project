"""
This is the rank system based on the regression model we built
"""

def survival_score(timeSurvived, duration, winPlace):

	"""
	survival_score = 80% * survival time score + 20% * win place score

	: type timeSurvived: int -- participant time survived
	: type duration: int  -- match duration time
	: type winPlace: int
	: rtype survival_score: int
	"""

	survival = (timeSurvived / duration) * 100
	if winPlace == 1:
		win_place = 100
	else:
		win_place = 100 - winPlace
	survival_score = int(survival * 0.8 + win_place * 0.2)
	if survival_score < 50:
		survival_score = 50

	return survival_score


def supply_score(pickups, pickupsfromcarepackages):

	"""
	supply_score = 80% * supply score + 20% * care packages score

	: type pickups: dict
	: type pickupsfromcarepackages: int
	: rtype supply_score: int
	"""

	# get the total number for each supply category
	Attachment = pickups["Attachment"] if "Attachment" in pickups else 0
	Use = pickups["Use"] if "Use" in pickups else 0
	Ammunition = pickups["Ammunition"] if "Ammunition" in pickups else 0
	Equipment = pickups["Equipment"] if "Equipment" in pickups else 0
	Weapon = pickups["Weapon"] if "Weapon" in pickups else 0

	#  calculate care package score
	if pickupsfromcarepackages > 0:
		care_package_score = 100
	else:
		care_package_score = 0

	#  calculate attachment score
	if Attachment <= 5:
		attachment_score = 50
	elif Attachment <= 9:
		attachment_score = 75
	else:
		attachment_score = 100

	# calculate use score
	if Use <= 5:
		use_score = 70
	elif Use <= 10:
		use_score = 85
	else:
		use_score = 100

	# calculate equipment score
	if Equipment <= 5:
		equipment_score = 75
	elif Equipment <= 10:
		equipment_score = 90
	else:
		equipment_score = 100

	# calculate weapon score
	if Weapon <= 1:
		weapon_score = 75
	elif Weapon == 2:
		weapon_score = 90
	else:
		weapon_score = 100

	# calculate ammunition score
	if Ammunition <= 5:
		ammunition_score = 50
	elif Ammunition <= 10:
		ammunition_score = 75
	elif Ammunition <= 14:
		ammunition_score = 90
	else:
		ammunition_score = 100

	supplies_score = (equipment_score + use_score + weapon_score + ammunition_score) * 0.225 + attachment_score * 0.1
	supply_score = int(supplies_score * 0.8 + care_package_score * 0.2)

	return supply_score


def damage_score(damageDealt):

	"""
	damage_score

	: type damageDealt: float
	: rtype damage_score: int
	"""

	if damageDealt >= 349.45:
		damage_score = 100
	elif damageDealt >= 300.54:
		damage_score = 95
	elif damageDealt >= 251.62:
		damage_score = 90
	elif damageDealt >= 216.7:
		damage_score = 85
	elif damageDealt >= 181.8:
		damage_score = 80
	elif damageDealt >= 146.89:
		damage_score = 75
	elif damageDealt >= 130.67:
		damage_score = 70
	elif damageDealt >= 114.47:
		damage_score = 65
	elif damageDealt >= 98.26:
		damage_score = 60
	elif damageDealt >= 86.19:
		damage_score = 55
	elif damageDealt >= 74.14:
		damage_score = 50
	else:
		damage_score = 45

	return damage_score


def kill_score(kills):

	"""
	kill_score

	: type kills: float
	: rtype kill_score: int
	"""

	if kills >= 2.95:
		kill_score = 100
	elif kills >= 2.51:
		kill_score = 95
	elif kills >= 2.04:
		kill_score = 90
	elif kills >= 1.71:
		kill_score = 85
	elif kills >= 1.38:
		kill_score = 80
	elif kills >= 1.06:
		kill_score = 75
	elif kills >= 0.91:
		kill_score = 70
	elif kills >= 0.77:
		kill_score = 65
	elif kills >= 0.65:
		kill_score = 60
	elif kills >= 0.54:
		kill_score = 55
	elif kills >= 0.43:
		kill_score = 50
	else:
		kill_score = 45

	return kill_score

def distance_score(walkDistance):

	"""
	distance_score

	: type walkDistance: float
	: rtype distance_score: int
	"""

	if walkDistance >= 5349.83:
		distance_score = 100
	elif walkDistance >= 4578.49:
		distance_score = 95
	elif walkDistance >= 3807.16:
		distance_score = 90
	elif walkDistance >= 3453.92:
		distance_score = 85
	elif walkDistance >= 3100.68:
		distance_score = 80
	elif walkDistance >= 2747.45:
		distance_score = 75
	elif walkDistance >= 2260.84:
		distance_score = 70
	elif walkDistance >= 1774.25:
		distance_score = 65
	elif walkDistance >= 1287.65:
		distance_score = 60
	elif walkDistance >= 879.20:
		distance_score = 55
	elif walkDistance >= 470.77:
		distance_score = 50
	else:
		distance_score = 45

	return distance_score
