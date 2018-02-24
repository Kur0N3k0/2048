import copy
import random

def welcome():
	message = ""
	message += """

 ,---.   ,--.    ,---. ,---.      ,-----.,--.             ,--.,--.                              
'.-.  \\ /    \\  /    ||  o  |    '  .--./|  ,---.  ,--,--.|  ||  | ,---. ,--,--,  ,---.  ,---.  
 .-' .'|  ()  |/  '  |.'   '.    |  |    |  .-.  |' ,-.  ||  ||  || .-. :|      \\| .-. || .-. : 
/   '-. \\    / '--|  ||  o  |    '  '--'\\|  | |  |\\ '-'  ||  ||  |\\   --.|  ||  |' '-' '\\   --. 
'-----'  `--'     `--' `---'      `-----'`--' `--' `--`--'`--'`--' `----'`--''--'.`-  /  `----' 
                                                                                 `---'          
	"""
	print message

def dump(maps):
	field = "{:4d} " * len(maps)
	for key in maps:
		print field.format(*key)

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

def rotation(maps, direction):
	if direction == RIGHT:
		result = copy.deepcopy(maps)
		for i in range(len(maps)):
			for k in range(len(maps[i])):
				result[i][k] = maps[k][i]
			result[i] = result[i][::-1]
		return result
	elif direction == LEFT:
		result = copy.deepcopy(maps)
		for i in range(len(maps)):
			for k in range(len(maps[i])):
				result[len(maps[i]) - 1 - i][k] = maps[k][i]
			result[i] = result[i]
		return result
	return []

def transition(maps, direction):
	if direction == LEFT:
		for i in range(0, len(maps)):
			for k in range(0, len(maps[i])):
				if maps[i][k] != 0 and k != 0:
					p = k
					while p - 1 >= 0 and maps[i][p - 1] == 0:
						maps[i][p - 1] = maps[i][p]
						maps[i][p] = 0
						p -= 1
		return maps
	elif direction == RIGHT:
		for i in range(0, len(maps)):
			for k in range(len(maps[i]) - 1, -1, -1):
				if maps[i][k] != 0 and k != len(maps[i]) - 1:
					p = k
					while p + 1 < len(maps[i]) and maps[i][p + 1] == 0:
						maps[i][p + 1] = maps[i][p]
						maps[i][p] = 0
						p += 1
		return maps
	return []

def calculate(maps, direction):
	if direction == LEFT:
		for i in range(len(maps)):
			for k in range(len(maps[i]) - 1):
				if maps[i][k] == maps[i][k + 1]:
					break
			if maps[i][k] == maps[i][k + 1]:
				maps[i][k] *= 2
				maps[i][k + 1] = 0
				transition(maps, direction)
		return maps
	elif direction == RIGHT:
		for i in range(len(maps)):
			for k in range(len(maps[i]) - 1, -1, -1):
				if maps[i][k] == maps[i][k - 1]:
					break
			if maps[i][k - 1] == maps[i][k]:
				maps[i][k] *= 2
				maps[i][k - 1] = 0
				transition(maps, direction)
		return maps
	return []

def value_generate(maps):
	num = 2
	if random.randint(0, 100) / 30 < 1: # 30% : 4
		num = 4

	# get 0 position
	zero_pos = []
	for i in range(len(maps)):
		for k in range(len(maps[i])):
			if maps[i][k] == 0:
				zero_pos.append([i, k])

	item = random.choice(zero_pos)
	maps[item[0]][item[1]] = num
	return maps

def map_generate(N):
	result = []
	for i in range(N):
		result.append([0] * N)
	result = value_generate(result)
	return value_generate(result)

def left(maps):
	maps = transition(maps, LEFT)
	maps = calculate(maps, LEFT)
	return value_generate(maps)

def right(maps):
	maps = transition(maps, RIGHT)
	maps = calculate(maps, RIGHT)
	return value_generate(maps)

def up(maps):
	maps = rotation(maps, RIGHT)
	maps = transition(maps, RIGHT)
	maps = calculate(maps, RIGHT)
	maps = rotation(maps, LEFT)
	return value_generate(maps)

def down(maps):
	maps = rotation(maps, RIGHT)
	maps = transition(maps, LEFT)
	maps = calculate(maps, LEFT)
	maps = rotation(maps, LEFT)
	return value_generate(maps)

maps = [[4, 0, 0, 0],
[0, 0, 0, 0],
[4, 0, 2, 0],
[4, 0, 0, 0]]
dump(maps)

maps = up(maps)
print ''
dump(maps)