import threading
import io
grid = [
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0],
		]
# Turns are either 'X' or 'O'
# pos is between 0 and 6

def opponent(token):
	if token == 'X':
		return 'O'
	return 'X'

def moove_wining(grid, x, y, token):
	def wins_vertial(grid, token, x, y):
		if y > 2:
			return False
		for i in range(1, 4):
			if grid[y + i][x] != token:
				return False
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

def can_play_here(grid, x):
	return grid[0][x] == 0

def play(grid, token, x):
	i = 0
	while i < len(grid) and grid[i][x] == 0:
		i += 1
	i -= 1
	grid[i][x] = token
	return i

def copy_gird(grid):
	grid2 = []
	for line in grid:
		grid2.append(line.copy())
	return grid2

def efficient(grid, token = 'X', max_depth = 7, depth = 0, isMyTurn = True, x = 0):
	if depth == max_depth:
		return 0
	if not can_play_here(grid, x):
		return 0

	grid_copy = copy_gird(grid)
	y = play(grid_copy, token, x)
	if moove_wining(grid_copy, x, y, token):
		if isMyTurn:
			return 7**(max_depth - depth)
		else:
			return -7**(max_depth - depth)
	res = 0
	for i in range(7):
		res += efficient(grid_copy, opponent(token), max_depth, depth + 1, not isMyTurn, i)

	return res

results = [0, 0, 0, 0, 0, 0, 0]
for i in range(7):
	results[i] = efficient(grid.copy(), 'O', 7, 0, True, i)

print(results.index(max(results)))
