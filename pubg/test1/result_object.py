"""
Result object collected the aggregated data which will be results shown on
the stats page
"""
class result_obj:

	def __init__(self):

		self.TotalAssists = 0
		self.LongestKill = 0
		self.TotalHeadshots = 0
		self.TotalWins = 0
		self.TotalLosses = 0
		self.TotalKills = 0
		self.TotalSuicides = 0
		self.TotalTeamkills = 0
		self.TotalDamageDealt = 0
		self.TotalWinPlace = 0
		self.TotalRevives = 0
		self.TotalGameCount = 0
		self.AverageKills = 0
		self.AverageDamageDealt = 0
		self.AverageWinPlace = 0
		self.TotalWalkDistance = 0
		self.AverageWalkDistance = 0
		self.WinRatio = 0
		self.TotalSurvivalScore = 0
		self.TotalSupplyScore = 0
		self.AverageSurvivalScore = 0
		self.AverageSupplyScore = 0
		self.Weapons = {}
		self.MostUsedWeapon = ''

	# aggregate retrived data from each match object to the result stats
	def aggregate(self, participant, survival_score, supply_score, weapon):
		self.TotalAssists += participant.assists
		self.LongestKill = max(self.LongestKill, participant.longestKill)
		self.TotalHeadshots += participant.headshotKills
		self.TotalWins += 1 if participant.winPlace == 1 else 0
		self.TotalLosses += 0 if participant.winPlace == 1 else 1
		self.TotalKills += participant.kills
		self.TotalSuicides += 1 if participant.deathType == "suicide" else 0
		self.TotalTeamkills += participant.teamKills
		self.TotalDamageDealt += participant.damageDealt
		self.TotalWinPlace += participant.winPlace
		self.TotalRevives += participant.revives
		self.TotalWalkDistance += participant.walkDistance
		self.TotalSurvivalScore += survival_score
		self.TotalSupplyScore += supply_score
		self.TotalGameCount += 1
		self.AverageKills = self.TotalKills/self.TotalGameCount
		self.AverageDamageDealt = self.TotalDamageDealt/self.TotalGameCount
		self.AverageWinPlace = self.TotalWinPlace/self.TotalGameCount
		self.WinRatio = self.TotalWins/self.TotalGameCount
		self.AverageWalkDistance = self.TotalWalkDistance/self.TotalGameCount
		self.AverageSurvivalScore = self.TotalSurvivalScore/self.TotalGameCount
		self.AverageSupplyScore = self.TotalSupplyScore/self.TotalGameCount
		self.Weapons[weapon] = self.Weapons.get(weapon,0) + 1
		if self.Weapons != {}:
			self.MostUsedWeapon = max(self.Weapons, key = self.Weapons.get)
