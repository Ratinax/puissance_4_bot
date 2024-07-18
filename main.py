import level0
import level2
import level1
from basic_functions import *

grid = [
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0],
		]

def invert_level(level):
	if level == level2:
		return level1
	return level2

# Player starting
level = level1

is_a_winner = False
token = 'X'
while not is_full(grid):
	x = level.get_move(grid, token)
	y = play(grid, token, x)
	print(f'{token} plays {x}, {y}')
	if moove_wining(grid, x, y, token):
		put_grid(grid)
		print(f'{token} won ! in {x}')
		is_a_winner = True
		break
	level = invert_level(level)
	token = opponent(token)
	put_grid(grid)

if not is_a_winner:
	print('it \'s a tie !')
