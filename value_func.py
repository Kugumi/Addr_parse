def value(key):
	@property
	def field(self):
		return getattr(self, key)

	return field

