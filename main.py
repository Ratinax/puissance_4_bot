grid = [
	[0,0,0,0,0,0,0],
	[0,'X',0,0,0,0,0],
	[0,0,'X',0,0,0,0],
	[0,0,0,'X',0,0,0],
	[0,0,0,0,'X',0,0],
	[0,0,0,0,0,'Y',0],
		]
# Turns are either 'X' or 'O'
# pos is between 0 and 6

def opponent(token):
	if token == 'X':
		return 'O'
	return 'X'

def moove_wining(grid, x):
	def getY(grid, x):
		y = 0
		while y < 5 and grid[y][x] == 0:
			y += 1
		return y
	def wins_vertial(grid, x, y):
		if y > 2:
			return False
		for i in range(0, 4):
			if grid[y + i][x] != grid[y][x]:
				return False
		return True
	def wins_horizontal(grid, x, y):
		return 4 * f'{grid[y][x]}' in ''.join(str(token) for token in grid[y])
	def wins_diagonal(grid, x, y):
		def getResultOfDiagonal(grid, x, y, xGrowing, yGrowing):
			yi = y
			xi = x
			diagonal = ""
			while yi != 5 * yGrowing != -1 and xi != 6 * xGrowing != -1:
				yi += yGrowing
				xi += xGrowing
			yGrowing = -yGrowing
			xGrowing = -xGrowing
			while yi != 5 * yGrowing != -1 and xi != 6 * xGrowing != -1:
				diagonal += str(grid[yi][xi])
				yi += yGrowing
				xi += xGrowing
			if 4 * f'{grid[y][x]}' in diagonal:
				return True
			return False
		return getResultOfDiagonal(grid, x, y, +1, +1) \
			+ getResultOfDiagonal(grid, x, y, +1, -1) \
			+ getResultOfDiagonal(grid, x, y, -1, +1) \
			+ getResultOfDiagonal(grid, x, y, -1, -1) \

	y = getY(grid, x)
	if wins_vertial(grid, x, y):
		return True
	if wins_horizontal(grid, x, y):
		return True
	if wins_diagonal(grid, x, y):
		return True
	return False

def can_play_here(grid, x):
	return grid[0][x] == 0

print(moove_wining(grid, 2))

# def find_best_moove(grid, turn = 'X') -> int:
# 	return

# def efficient(grid, token = 'X', max_depth = 4, depth = 0, isMyTurn = True, x = 0):
# 	if depth == max_depth:
# 		return 0
# 	# TODO play
# 	# If win
# 		# IF mon tour
# 			# TODO return 7**(max_depth - depth)
# 		# ELSE
# 			# TODO return - 7**(max_depth - depth)
# 	res = 0
# 	for i in range(7):
# 		res += efficient(grid, otherToken, max_depth, depth + 1, not isMyTurn, i)
# 	return res
