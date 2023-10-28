def my_steps(n):
	if not 1 <= n <= 25:
		raise ValueError("Input out of bounds.")
	climbing_steps = [0] * (n+1)
	climbing_steps[0] = 1
	for i in range(1, n+1):
		climbing_steps[i] = climbing_steps[i-1] + climbing_steps[i-2]
	return climbing_steps[n]
