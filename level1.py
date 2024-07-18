from basic_functions import *
import level0
import random

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

def get_connections(grid, x, y):
	connections = 0
	i = 1
	for _ in range(8):
		res = 1
		tmp_x = x
		tmp_y = y
		tmp_x, tmp_y = slide(tmp_x, tmp_y, COMBINATIONS[i])
		if (0 <= tmp_x < 7) and (0 <= tmp_y < 6):
			token = grid[tmp_y][tmp_x]

		while (0 <= tmp_x < 7) and (0 <= tmp_y < 6) and grid[tmp_y][tmp_x] != 0 and grid[tmp_y][tmp_x] == token:
			res <<= 1
			tmp_x, tmp_y = slide(tmp_x, tmp_y, COMBINATIONS[i])
		connections += res
		i <<= 1
	return connections

def find_most_connecting(grid, token):
	max_connections = []
	res = []
	for i in range(7):
		if not can_play_here(grid, i):
			continue
		grid_tmp = copy_gird(grid)
		y = play(grid_tmp, token, i)
		connections = get_connections(grid, i, y)
		if len(max_connections) == 0 or connections == max(max_connections):
			max_connections.append(connections)
			res.append(i)
		elif connections > max(max_connections):
			max_connections = [connections]
			res = [i]
	# print(res)
	return random.choice(res)


def get_move(grid, token):
	# Win if i can
	for i in range(7):
		if not can_play_here(grid, i):
			continue
		grid_tmp = copy_gird(grid)
		y = play(grid_tmp, token, i)
		if moove_wining(grid_tmp, i, y, token):
			return i

	# Avoid opponent from winning
	token = opponent(token)
	for i in range(7):
		if not can_play_here(grid, i):
			continue
		grid_tmp = copy_gird(grid)
		y = play(grid_tmp, token, i)
		if moove_wining(grid_tmp, i, y, token):
			return i
	return find_most_connecting(grid, token)