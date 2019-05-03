"""
Player objects contain information about a player and a list of their recent
matches (up to 14 days old).
Note: player objects are specific to platform shards.
"""
class player_obj:

	def __init__(self, data):

		"""
		data is the response from pubg api after sending get request using player object url
		"""

		self.id = data['data'][0]['id']
		self.name = data['data'][0]['attributes']['name']
		self.shardId = data['data'][0]['attributes']['shardId']
		self.match_list = data['data'][0]['relationships']['matches']['data']
