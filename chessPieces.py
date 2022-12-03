import re
from turtle import color

class Pawn():
	#Each Pawn advances one square at a time 
	def possible_moves (board, coordinates):
		possible_moves = []
		x = coordinates[0]
		y = coordinates[1]

		if(re.match('black+', board[x][y])):
			#Move Downwards
			if(x+1 < 8 and board[x+1],[y] == "     X     "):
				possible_moves.append((x+1, y))

			#Diagonal
			if(x+1 < 8 and y+1 < 8 and re.match(color, board[x+1][y+1])):
				possible_moves.append((x+1, y+1))
			if(x+1 < 8 and y-1 >= 0 and re.match(color, board[x+1][y-1])):
				possible_moves.append((x+1, y-1))

		if (x-1 >= 0 and re.match('white', board[x][y])):
			#Move Upwards
			if(board[x-1][y] == "     X     "):
				possible_moves.append((x-1,y))

			#Diagonal
			if(x-1 >= 0 and y+1 < 8 and re.match( color, board[x-1][y-1])):
				possible_moves.append((x-1,y+1))
			if(x-1 >= 0 and y-1 >= 0 and re.match( color , board[x-1][y-1])):
				possible_moves.append((x-1,y-1))

		return possible_moves

class Rook():
	#Rook only moves in a straight horizontal/vertical line 
	def possible_moves(board, coordinates):
		possible_moves=[[],[]]
		x = coordinates[0]
		y = coordinates[1]

		if(re.match('black+', board[x][y])):
			pattern = 'white+'
			color = 'black+'
		else:
			pattern = 'black+'
			color = 'white+'

		for i in range(x, 8):
			#Move Downwards
			if (i+1 < 8):
				if(re.match(color,board[i+1][y])):
					break
				possible_moves[0].append(i+1)
				possible_moves[1].append(y)
				if(re.match(pattern,board[i-1][y])):
					break

		for i in range(x,0,-1):
			#Move Upwards
			if(i-1 >= 0):
				if(re.match(color, board[i-1][y])):
					break
				possible_moves[0].append(i-1)
				possible_moves[1].append(y)
				if(re.match(pattern, board[i-1][y])):
					break

		for i in range(y,0,-1):
			#Move Left-side
			if(i-1 >= 0):
				if(re.match(color, board[x][i-1])):
					break
				possible_moves[0].append(x)
				possible_moves[1].append(i-1)
				if(re.match(pattern, board[x][i-1])):
					break

		for i in range(y, 8):
			#Move Right-side
			if (i+1 < 8):
				if(re.match(color,board[x][i+1])):
					break
				possible_moves[0].append(x)
				possible_moves[1].append(i+1)
				if(re.match(pattern,board[x][i+1])):
					break

		return list(zip(possible_moves[0],possible_moves[1]))

class Bishop():
	# Bishop can only move Move Diagonally right (upwards) or Diagonally left (downwards)
	def possible_moves(board, coordinates):
		possible_moves=[[],[]]
		x = coordinates[0]
		y = coordinates[1]
		if(re.match('black+', board[x][y])):
			pattern = 'white+'
			color = 'black+'
		else:
			pattern = 'black+'
			color = 'white+'

		while(x-1 >= 0 and y+1  < 8):
			#Move Diagonally right (upwards)
			if(re.match(color,board[x-1][y+1])):
					break
			possible_moves[0].append(x-1)
			possible_moves[1].append(y+1)
			if(re.match(pattern,board[x-1][y+1])):
				break
			x -= 1
			y += 1

		while(x+1 < 8 and y-1  >= 0):
			#Move Diagonally left (downwards)
			if(re.match(color,board[x+1][y-1])):
					break
			possible_moves[0].append(x+1)
			possible_moves[1].append(y-1)
			if(re.match(pattern,board[x+1][y-1])):
				break
			x += 1
			y -= 1

		return list(zip(possible_moves[0],possible_moves[1]))	


class King():
	#King (Black) moves 2 squares downwards while King (White) moves 2 squares upwards or they can both move left or right 
	def possible_moves (board, coordinates):
		possible_moves = []
		x = coordinates[0]
		y = coordinates[1]

		if(re.match('black+', board[x][y])):
			#Move Downwards
			if(x+2 < 8 and board[x+2],[y] == "     X     "):
				possible_moves.append((x+2, y))

		if (x-2 >= 0 and re.match('white', board[x][y])):
			#Move Upwards
			if(board[x-2][y] == "     X     "):
				possible_moves.append((x-2,y))

		for i in range(y,2,-1):
			#Move Left-side
			if(i-2 > 0 and board[x][i-2] == "     X     "):
				possible_moves.append((x, i-2))

		for i in range(y,2,8):
			#Move Right-side
			if (i+2 < 8 and board[x][i+1] == "     X     "):
				possible_moves.append((x, i+2))
		
		return possible_moves

	
class Queen():
	#Queen is free to move in any direction and take as many steps as she wants  
	def possible_moves(board, coordinates):
		possible_moves=[[],[]]
		x = coordinates[0]
		y = coordinates[1]

		if(re.match('black+', board[x][y])):
			pattern = 'white+'
			color = 'black+'
		else:
			pattern = 'black+'
			color = 'white+'

		for i in range(x, 8):
			#Move Downwards
			if (i+1 < 8):
				if(re.match(color,board[i+1][y])):
					break
				possible_moves[0].append(i+1)
				possible_moves[1].append(y)
				if(re.match(pattern,board[i+1][y])):
					break

		for i in range(x,0,-1):
			#Move Upwards
			if(i-1 >= 0):
				if(re.match(color, board[i-1][y])):
					break
				possible_moves[0].append(i-1)
				possible_moves[1].append(y)
				if(re.match(pattern, board[i-1][y])):
					break

		for i in range(y,0,-1):
			#Move Left-side
			if(i-1 >= 0):
				if(re.match(color, board[x][i-1])):
					break
				possible_moves[0].append(x)
				possible_moves[1].append(i-1)
				if(re.match(pattern, board[y][i-1])):
					break

		for i in range(y, 8):
			#Move Right-side
			if (i+1 < 8):
				if(re.match(color,board[x][i+1])):
					break
				possible_moves[0].append(x)
				possible_moves[1].append(i+1)
				if(re.match(pattern,board[y][i+1])):
					break

		while(x-1 >=0 and y-1 >=0):
			#Move Diagonally left (upwards)
			if(re.match(color,board[x-1][y-1])):
					break
			possible_moves[0].append(x-1)
			possible_moves[1].append(y-1)
			x -= 1
			y -= 1
			if(re.match(pattern,board[x-1][y-1])):
				break

		while(x-1 >=0 and y+1  < 8):
			#Move Diagonally right (upwards)
			if(re.match(color,board[x-1][y+1])):
					break
			possible_moves[0].append(x-1)
			possible_moves[1].append(y+1)
			if(re.match(pattern,board[x-1][y+1])):
				break
			x -= 1
			y += 1

		while(x+1 < 8 and y-1  >=0 ):
			#Move Diagonally left (downwards)
			if(re.match(color,board[x+1][y-1])):
					break
			possible_moves[0].append(x+1)
			possible_moves[1].append(y-1)
			if(re.match(pattern,board[x+1][y-1])):
				break
			x += 1
			y -= 1

		while(x+1  < 8 and y+1  < 8):
			#Move Diagonally right (downwards)
			if(re.match(color,board[x+1][y+1])):
					break
			possible_moves[0].append(x+1)
			possible_moves[1].append(y+1)
			if(re.match(pattern,board[x+1][y+1])):
				break
			x += 1
			y += 1
		return list(zip(possible_moves[0],possible_moves[1]))





