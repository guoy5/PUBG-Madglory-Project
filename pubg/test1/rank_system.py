class rank_obj:

	def __init__(self):
		self.supply_score = 0
		self.kill_score = 0
		self.damage_score = 0
		self.distance_score = 0
		self.survival_score = 0
		self.final_score = ''

	# rank letter ranges
	def final_rank(self):
		score = (self.supply_score + self.kill_score + self.damage_score + self.distance_score + self.survival_score)/5

		if score > 95:
			self.final_score = 'S+'
		elif score > 90:
			self.final_score = 'S'
		elif score > 85:
			self.final_score = 'S-'
		elif score > 80:
			self.final_score = 'A+'
		elif score > 75:
			self.final_score = 'A'
		elif score > 70:
			self.final_score = 'A-'
		elif score > 65:
			self.final_score = 'B+'
		elif score > 60:
			self.final_score = 'B'
		elif score > 55:
			self.final_score = 'B-'
		elif score > 50:
			self.final_score = 'C+'
		elif score > 45:
			self.final_score = 'C'
		else:
			self.final_score = 'C-'
