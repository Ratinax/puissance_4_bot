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
level = level2

is_a_winner = False
token = 'X'
is_player_turn = True
player_game = False

while not is_full(grid):
	if player_game and is_player_turn:
		x = int(input('Enter a column number to play: '))
		while not can_play_here(grid, x):
			x = int(input('Enter a valid column number to play: '))
	else:
		x = level.get_move(grid, token)
	y = play(grid, token, x)
	print(f'{token} plays {x}, {y}')
	if moove_wining(grid, x, y, token):
		put_grid(grid)
		print(f'{token} won ! in {x}')
		is_a_winner = True
		break
	if not player_game:
		level = invert_level(level)
	else:
		is_player_turn = not is_player_turn
	token = opponent(token)
	put_grid(grid)

if not is_a_winner:
	print('it \'s a tie !')
