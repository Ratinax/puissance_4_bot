import threading
import io
from basic_functions import *
from math import inf

# Turns are either 'X' or 'O'
# pos is between 0 and 6

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

def get_move(grid, token):
	results = [0, 0, 0, 0, 0, 0, 0]
	for i in range(7):
		results[i] = efficient(grid.copy(), token, 4, 0, True, i)
	for i in range(7):
		if not can_play_here(grid, i):
			results[i] = -inf
	return results.index(max(results))