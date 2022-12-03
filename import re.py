import re

class Pawn():

#Each Pawn advances one square at a time after the first move
	def possible_moves (board, coordinates):
		possible_moves = []
		x = coordinates[0]
		y = coordinates[1]

		if(re.match('black+', board[x][y])):
			#Move Downwards
			if(x+1 < 8 and board[x+1],[y] == '   __   '):
				possible_moves.append((x+1, y))

			#Diagonal
			if(x+1 < 8 and y+1 < 8 and re.match('white', board[x+1][y+1])):
				possible_moves.append((x+1, y+1))
			if(x+1 < 8 and y-1 >= 0 and re.match('white', board[x+1][y-1])):
				possible_moves.append((x+1, y-1))
		if (x-1 >= 0 and re.match('white', board[x][y])):
			#Move Upwards
			if(board[x-1][y] == '   __   '):
				possible_moves.append((x-1,y))

			#Diagonal
			if(x-1 >= 0 and y+1 < 8 and re.match('black', board[x-1][y-1])):
				possible_moves.append((x-1,y+1))
			if(x-1 >= 0 and y-1 >= 0 and re.match('black', board[x-1][y-1])):
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

		while(x-1 >=0 and y+1  < 8):
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


class King():

#King moves 2 squares in any direction while no piece is blocking his path 
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
			if (i+2 < 8):
				if(re.match(color,board[i+2][y])):
					break
				possible_moves[0].append(i+2)
				possible_moves[1].append(y)
				break

		for i in range(x,0,-1):
			#Move Upwards
			if(i-2 >= 0):
				if(re.match(color, board[i-2][y])):
					break
				possible_moves[0].append(i-2)
				possible_moves[1].append(y)
				break

		for i in range(y,0,-1):
			#Move Left-side
			if(i-2 >= 0):
				if(re.match(color, board[x][i-2])):
					break
				possible_moves[0].append(x)
				possible_moves[1].append(i-2)
				break

		for i in range(y, 8):
			#Move Right-side
			if (i+1 < 8):
				if(re.match(color,board[x][i+2])):
					break
				possible_moves[0].append(x)
				possible_moves[1].append(i+2)
				break

        if(x - 2 >= 0 and coordenation[1] - 2 >= 0 and not(re.match(color,board[ x - 2][ y - 2]))):
             possibleMoves[0].append(x - 2)
             possibleMoves[1].append(y - 2)
        if(x - 2 >= 0 and y + 2 < 8 and not(re.match(color,board[x - 2][y + 2]))):
             possibleMoves[0].append(x - 2)
             possibleMoves[1].append(y + 2)
        if(x + 2 < 8 and y - 2 >= 0 and not(re.match(color,board[x + 2][ y - 2]))):
             possibleMoves[0].append(x + 2)
             possibleMoves[1].append(y - 2)
        if( x + 2 < 8 and y + 2 < 8 and not(re.match(color,board[ x + 2][ y + 2]))):
             possibleMoves[0].append(x + 2)
             possibleMoves[1].append(y + 2)

		return list(zip(possible_moves[0],possible_moves[1]))

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

		while(x-1 >=0 and y+1  < 8):
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





