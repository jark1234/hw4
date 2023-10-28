def allcaps(func):
	def caps():
		result = func()
		return result.upper()
	return caps
