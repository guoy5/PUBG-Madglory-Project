import datetime

"""
Match objects contain information about a completed match such as the game mode
played, duration, and which players participated.
"""

class match_obj:

	def __init__(self, data):

		"""
		data is the response from pubg api after sending get request using match object url
		"""

		self.id = data['data']['id']
		self.createdAt = datetime.datetime.strptime(data['data']['attributes']['createdAt'], "%Y-%m-%dT%H:%M:%SZ")
		self.duration = data['data']['attributes']['duration']
		self.gameMode = data['data']['attributes']['gameMode']
		self.mapName = data['data']['attributes']['mapName']
		self.isCustomMatch = data['data']['attributes']['isCustomMatch']
		self.seasonState = data['data']['attributes']['seasonState']
		self.shardId = data['data']['attributes']['shardId']
		self.asset_id = data['data']['relationships']['assets']['data'][0]['id']
		self.included = data['included']
		self.telemetry_url = ''
