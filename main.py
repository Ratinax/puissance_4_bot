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
	def wins_vertial(grid, x, y):
		if y > 2:
			return False
		for i in range(0, 4):
			if grid[y + i][x] != token:
				return False
		return True
	def wins_horizontal(grid, y):
		return 4 * token in ''.join(str(token) for token in grid[y])
	def wins_diagonal(grid, x, y):
		def getResultOfDiagonal(grid, x, y, xGrowing, yGrowing):
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
			if 4 * f'{grid[y][x]}' in diagonal:
				return True
			return False
		if getResultOfDiagonal(grid, x, y, +1, +1) : return True
		if getResultOfDiagonal(grid, x, y, +1, -1) : return True
		if getResultOfDiagonal(grid, x, y, -1, +1) : return True
		if getResultOfDiagonal(grid, x, y, -1, -1) : return True

	if wins_vertial(grid, x, y):
		return True
	if wins_horizontal(grid, y):
		return True
	if wins_diagonal(grid, x, y):
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
	if depth == 0:
		results[x] = res
		pass
	else:
		return res

results = [0, 0, 0, 0, 0, 0, 0]
threads = []
for i in range(7):
	thread = threading.Thread(target=efficient, args=(grid.copy(), 'O', 6, 0, True, i))
	threads.append(thread)
	thread.start()
	# results.append(efficient(grid, token = 'O', x = i))
for thread in threads:
	thread.join()
print(results)
