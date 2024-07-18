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

COMBINATIONS = {
	1: (0, 1),
	2: (0, -1),
	4: (1, 0),
	8: (-1, 0),
	16: (-1, 1),
	32: (1, -1),
	64: (1, 1),
	128: (-1, -1),
}

def slide(x, y, vector):
	x += vector[0]
	y += vector[1]
	return x, y

def slide_invert(x, y, vector):
	x -= vector[0]
	y -= vector[1]
	return x, y

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
		i = 1
		for _ in range(8):
			res = 0

			tmp_x, tmp_y = slide_invert(x, y, COMBINATIONS[i])
			while (0 <= tmp_x < 7) and (0 <= tmp_y < 6) and grid[tmp_y][tmp_x] == token:
				tmp_x, tmp_y = slide_invert(tmp_x, tmp_y, COMBINATIONS[i])

			tmp_x, tmp_y = slide(tmp_x, tmp_y, COMBINATIONS[i])
			while (0 <= tmp_x < 7) and (0 <= tmp_y < 6) and grid[tmp_y][tmp_x] == token:
				res += 1
				tmp_x, tmp_y = slide(tmp_x, tmp_y, COMBINATIONS[i])

			if res >= 4:
				return True
			i <<= 1
		return False

	if wins_vertial(grid, token, x, y):
		return True
	if wins_horizontal(grid, token, y):
		return True
	if wins_diagonal(grid, token, x, y):
		return True
	return False