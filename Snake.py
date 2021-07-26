import readchar
import os
import random

POS_X = 0
POS_Y = 1

MAP_WIDTH = 20
MAP_HEIGHT = 15
NUM_OF_NUMBER_OBJECTS = 10

tail_length = 1
tail = []
my_position = [random.randint(1,MAP_WIDTH-1),random.randint(1,MAP_HEIGHT-1)]
map_objects = []
while len(map_objects) < NUM_OF_NUMBER_OBJECTS:
	new_position = [random.randint(1,MAP_WIDTH-1),random.randint(1,MAP_HEIGHT-1)]
	if new_position not in map_objects and new_position != my_position:
		map_objects.append(new_position)

while True:
	os.system("cls")
	print("+" + "-" * MAP_WIDTH * 3 + "+" )
	for cordinate_y in range(MAP_HEIGHT):
		
		print("|", end="")
		
		for cordinate_x in range(MAP_WIDTH):
			
			char_to_draw = " "
			
			for map_object in map_objects:
				if map_object == list([cordinate_x,cordinate_y]):
					char_to_draw = "o"

			for tail_piece in tail:
				if tail_piece == list([cordinate_x,cordinate_y]):
					char_to_draw = "■"
					
			if my_position == list([cordinate_x,cordinate_y]):
				char_to_draw = "■"
			
			if my_position in map_objects:
				map_objects.remove(my_position)
				tail_length += 1
			print(" {} ".format(char_to_draw),end="")
		print("|")	
	print("+" + "-" * MAP_WIDTH * 3 + "+")

	# Ask user where to move
	#direction = input("A donde te quieres mover? [WASD] [Q to left]: ") #Now is not used
	print("A donde te quieres mover? [WASD] [Any other letter to quit]")
	direction = readchar.readchar().decode()

	if direction.upper() == "W":
		my_position[POS_Y] -= 1
		my_position[POS_Y] %= MAP_HEIGHT
	elif direction.upper() == "S":
		my_position[POS_Y] += 1
		my_position[POS_Y] %= MAP_HEIGHT
	elif direction.upper() == "A":
		my_position[POS_X] -= 1
		my_position[POS_X] %= MAP_WIDTH
	elif direction.upper() == "D":
		my_position[POS_X] += 1
		my_position[POS_X] %= MAP_WIDTH
	else:
		exit()

	tail.insert(0,my_position.copy())
	tail = tail[:tail_length]
	
	#If you want sanke to stops in the walls then use this
	"""
	if direction.upper() == "W" and ((my_position[POS_Y] - 1) > -1):
		my_position[POS_Y] -= 1
	elif direction.upper() == "S" and ((my_position[POS_Y] + 1) < MAP_HEIGHT):
		my_position[POS_Y] += 1
	elif direction.upper() == "A" and ((my_position[POS_X] - 1) > -1):
		my_position[POS_X] -= 1
	elif direction.upper() == "D" and ((my_position[POS_X] + 1) < MAP_WIDTH):
		my_position[POS_X] += 1
	elif direction.upper() == "Q":
		exit(0)
	"""