

class Crime:

	def __init__(self, offense):
		self.lat = offense['location']['latitude']
		self.lng = offense['location']['longitude']
		self.description = offense['summarized_offense_description']
		self.start_time = offense['occurred_date_or_date_range_start']

	def get_location(self):
		return (self.lat, self.lng)
