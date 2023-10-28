def my_steps(n):
	if not 1 <= n <= 25:
		raise ValueError("Input out of bounds.")
	climbing = [0] * (n+1)
	climbing[0] = 1
	for i in range(1, n+1):
		climbing[i] = climbing[i-1] + climbing[i-2]
	return climbing[n]

