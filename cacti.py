def cacti_number(func):
	def array(grid):
		total_rows = len(grid)
		total_cols = len(grid[0])
		cacti_count = 0
		for row in range(total_rows):
			for col in range(total_cols):
				if grid[row][col] ==0:
					is_adjacent_empty = True
					for i in range(max(0, row - 1), min(total_rows, row+2)):
						for j in range(max(0, col - 1), min (total_cols, col + 2)):
							if grid[i][j] == 1:
								is_adjacent_empty = False
								break
						if not is_adjacent_empty:
							break
					if is_adjacent_empty:
						cacti_count +=1
		return cacti_count
	return array
