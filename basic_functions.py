def can_play_here(grid, x):
	return grid[0][x] == 0

def play(grid, token, x):
	i = 0
	while i < len(grid) and grid[i][x] == 0:
		i += 1
	i -= 1
	grid[i][x] = token
	return i

def opponent(token):
	if token == 'X':
		return 'O'
	return 'X'

def is_full(grid):
	for i in range(7):
		if can_play_here(grid, i):
			return False
	return True

def copy_gird(grid):
	grid2 = []
	for line in grid:
		grid2.append(line.copy())
	return grid2

def put_grid(grid):
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j] == 0:
				print('|_|', end='')
			else:
				print(f'|{grid[i][j]}|', end='')
		print()
	print()

def moove_wining(grid, x, y, token):
	def wins_vertial(grid, token, x, y):
		if y > 2:
			return False
		for i in range(1, 4):
			if grid[y + i][x] != token:
				return False
		# print('here')
		return True
	def wins_horizontal(grid, token, y):
		if grid[y][3] != token: return False
		return 4 * token in ''.join(str(token) for token in grid[y])
	def wins_diagonal(grid, token, x, y):
		def getResultOfDiagonal(grid, token, x, y, xGrowing, yGrowing):
			if not token in grid[2]:
				return False
			yi = y
			xi = x
			diagonal = ""
			yLimit = 5 * (yGrowing != -1)
			xLimit = 6 * (xGrowing != -1)
			while yi != yLimit and xi != xLimit:
				yi += yGrowing
				xi += xGrowing
			yGrowing = -yGrowing
			xGrowing = -xGrowing
			yLimit = 5 * (yGrowing != -1)
			xLimit = 6 * (xGrowing != -1)
			while yi != yLimit and xi != xLimit:
				diagonal += str(grid[yi][xi])
				yi += yGrowing
				xi += xGrowing
			if 4 * token in diagonal:
				return True
			return False
		if getResultOfDiagonal(grid, token, x, y, +1, +1) : return True
		if getResultOfDiagonal(grid, token, x, y, +1, -1) : return True
		if getResultOfDiagonal(grid, token, x, y, -1, +1) : return True
		if getResultOfDiagonal(grid, token, x, y, -1, -1) : return True

	if wins_vertial(grid, token, x, y):
		return True
	if wins_horizontal(grid, token, y):
		return True
	if wins_diagonal(grid, token, x, y):
		return True
	return False