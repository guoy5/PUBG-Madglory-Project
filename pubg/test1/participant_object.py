"""
Participant objects represent a player in the context of a match. Participant
objects are only meaningful within the context of a match and are not exposed
as a standalone resource.
"""
class participant_obj:

	def __init__(self, data):
		"""
		data is the particpant object retrived from match included array
		"""
		self.DBNOs = data['DBNOs']
		self.assists = data['assists']
		self.boosts = data['boosts']
		self.damageDealt = data['damageDealt']
		self.deathType = data['deathType']
		self.headshotKills = data['headshotKills']
		self.heals = data['heals']
		self.killPlace = data['killPlace']
		self.killStreaks = data['killStreaks']
		self.kills = data['kills']
		self.longestKill = data['longestKill']
		self.name = data['name']
		self.playerId = data['playerId']
		self.revives = data['revives']
		self.rideDistance = data['rideDistance']
		self.roadKills = data['roadKills']
		self.swimDistance = data['swimDistance']
		self.teamKills = data['teamKills']
		self.timeSurvived = data['timeSurvived']
		self.vehicleDestroys = data['vehicleDestroys']
		self.walkDistance = data['walkDistance']
		self.weaponsAcquired = data['weaponsAcquired']
		self.winPlace = data['winPlace']
