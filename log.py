import time
def timestamp(func):
	def timetest(*args, **kwargs):
		print(time.ctime())
		result = func(*args, **kwargs)
		return result
	return timetest
