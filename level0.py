from basic_functions import *
from random import randint

def get_move(grid, token):
	disponible_columns = []
	for i in range(7):
		if can_play_here(grid, i):
			disponible_columns.append(i)
	return disponible_columns[randint(0, len(disponible_columns) - 1)]

