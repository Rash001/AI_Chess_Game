from optparse import Option
import numpy as np
import random as rd

# pieces for a standard - 8x8 chessboard
black_piece = ['BK ','BQ ','BP1','BP2','BP3','BP4','BP5','BP6','BP7','BP8','BR1','BR2','BR3','BR4','BB1','BB2']
white_piece = ['WK ','WQ ','WP1','WP2','WP3','WP4','WP5','WP6','WP7','WP8','WR1','WR2','WR3','WR4','WB1','WB2']

# pieces for different states ( Minichess - 4X4 chessboard)
black_piece_mini = [['BK ','BQ ','BP1','BP2'],['BK ','BQ ','BR1','BR2'],['BK ','BQ ','BR1','BP2'],['BK ','BQ ','BP1','BP2']]
white_piece_mini = [['WK ','WQ ','WP1','WP2'],['WK ','WQ ','WR1','WR2'],['WK ','WQ ','WR1','WP2'],['WK ','WQ ','WR1','WR2']]

#row and column markers for every cell within the chessboard
rows = [str(num+1) for num in range(8)]
columns = ['A','B','C','D','E','F','G','H'] 

class chessboardState():
	def __init__ (self, minichess = 'False', minitype = 0 ):
		self.minichess = minichess
		self.minitype = minitype - 2
		#minichess game
		if(minichess == 'True'):
			self.size = 'MiniSize'
			self.rows = rows[0:4]
			self.columns = columns [0:4]
			self.shape = (4,4)
			self.chessboard = np.empty((4,4),dtype = 'S3')
			for r in range(0,4):
				for c in range(0,4):
					self.chessboard[r,c] = '   '
			self.pieces = []
			for piece in white_piece_mini[minitype - 2] + black_piece_mini[minitype - 2]:
				self.pieces.append(chessPieces(piece, self.size))
			for new_piece in self.pieces:
				r, c = new_piece.pos_index()
				self.chessboard[r, c] = new_piece.str_name()
		#standard chess game
		else:
			self.size = 'StandardSize' 
			self.columns = columns
			self.rows = rows
			self.shape = (8,8)
			self.chessboard = np.empty((8, 8), dtype='S3') 
			for r in range(0,8):
				for c in range(0,8):
					self.chessboard[r, c] = '   '
			self.pieces = []
			for piece in white_piece + black_piece:
				self.pieces.append(chessPieces(piece,self.size)) 
			for new_piece in self.pieces:
				r, c = new_piece.pos_index()
				self.chessboard[r, c] = new_piece.str_name()

	def showChessBoard(self):
		if self.size == 'MiniSize':
			print('|=====================|')
			print('|  | A | B | C | D |  |')
			print('|---------------------|')
			for row in range(4):
				print('| ' + str(4 - row), end='|')
				for col in range(4):
					print(str(self.chessboard[row, col], encoding='utf-8'), end='|')
				print(str(4 - row) + ' |')
			print('|---------------------|')
			print('|  | A | B | C | D |  |')
			print('|=====================|')
		else:
			print('|===================================|')
			print('|   A | B | C | D | E | F | G | H   |')
			print('|-----------------------------------|')
			for row in range(8):
				print(' ' + str(8 - row), end='|')
				for col in range(8):
					print(str(self.chessboard[row, col], encoding='utf-8'), end='|')
				print(str(8 - row) + ' ')
			print('|-----------------------------------|')
			print('|   A | B | C | D | E | F | G | H   |')
			print('|===================================|')

	def pick_piece(self, picked): 
		#pick the chess piece given the list of pieces 
		if(picked in ['BK','BQ','WK','WQ']): 
			picked += ' ' #mandate space
		for playing in self.pieces:
			if(picked == playing.str_name()):
				return playing
		return 0

	def move_piece(self, piece, goal):
		#function to get the moves of each piece Eg., BP1 (piece) and H7 (position index of destination)
		flag= 0 #success flag
		capture = 0
		if (piece in ['BK', 'BQ', 'WK', 'WQ']):
			piece += ' ' # mandate space
		for current_piece in self.pieces:
			if(piece == current_piece.str_name()): 
				prev_row, prev_col = current_piece.pos_index()
				dest_row, dest_col = pos_toint(goal)
				if (self.size == 'MiniSize'):
					dest_row = 4 - int(goal[1])
				#validating the piece to be of different color than its oponent while it is captured
				if (str(self.chessboard[dest_row, dest_col], encoding='utf-8') != '   '):
					if(self.pick_piece(str(self.chessboard[dest_row,dest_col], encoding='utf-8')).player == current_piece.player):
						return 0
					else:
						capture = 1
				possible_move, path_of_move = current_piece.possible_moves(goal,capture)
				if(possible_move == 1):
					for (row, col) in path_of_move: 
						if (str(self.chessboard[row, col], encoding='utf-8') != '   '):
							return 0
					new_row, new_col =current_piece.pos_index() 
					self.chessboard[prev_row,prev_col] = '   ' 
					if(str(self.chessboard[new_row,new_col],encoding='utf-8') != '   '):
						self.capture_piece(str(self.chessboard[new_row,new_col],encoding='utf-8'))
					self.chessboard[new_row,new_col] = current_piece.str_name()
					flag = 1 #Move successfull
				break
		return flag
	
	def capture_piece(self,captured): 
		#function to eliminate the captured piece
		capture_list = []
		for playing in self.pieces:
			if(captured != playing.str_name()):
				capture_list.append(playing)
		self.pieces = capture_list
		return 0
	
	def possible_checkmateMove(self,current_piece,goal): 
		flag, path_of_move = current_piece.RulesEnforced(goal)
		if (flag == 1):
			for (row, col) in path_of_move:
				if (str(self.chessboard[row, col], encoding='utf-8') != '   '):
					return 0
		return flag

	
	def possible_checkmateMoveAI(self,current_piece,goal):
		flag, path_of_move = current_piece.RulesEnforced(goal)
		pre_row, pre_col = current_piece.pos_index()
		dest_row, dest_col = pos_toint(goal)
		if (self.size == 'MiniSize'): 
			dest_row = 4 - int(goal[1])
		if(current_piece.type == 'Pawn'):
			if (current_piece.pieceName[0] == 'B'):
				if ((abs(dest_col - pre_col) == 1) and (dest_row - pre_row == 1)):
					if (str(self.chessboard[dest_row, dest_col], encoding='utf-8') != '   '):  
						if (self.pick_piece(str(self.chessboard[dest_row, dest_col], encoding='utf-8')).player != current_piece.player):
							return 1
				elif ((abs(dest_col - pre_col) == 0) and (dest_row - pre_row == 1)):
					if (str(self.chessboard[dest_row, dest_col], encoding='utf-8') != '   '):
						return 0
					else:
						return 1
				elif((current_piece.moves == 0) and (abs(dest_col - pre_col) == 0) and (dest_row - pre_row == 2)):
					if (str(self.chessboard[dest_row, dest_col], encoding='utf-8') != '   '):
						return 0
					elif(str(self.chessboard[dest_row - 1, dest_col], encoding='utf-8') != '   '):
						return 0
					else:
						return 1
			elif(current_piece.pieceName[0] == 'W'):
				if((abs(dest_col - pre_col) == 1) and (dest_row - pre_row == -1)):
					if (str(self.chessboard[dest_row, dest_col], encoding='utf-8') != '   '):  
						if (self.pick_piece(str(self.chessboard[dest_row, dest_col], encoding='utf-8')).player != current_piece.player):
							return 1
				elif((abs(dest_col - pre_col) == 0) and (dest_row - pre_row == -1)):
					if (str(self.chessboard[dest_row, dest_col], encoding='utf-8') != '   '):
						return 0
					else:
						return 1
				elif((current_piece.moves == 0) and (abs(dest_col - pre_col) == 0) and (dest_row - pre_row == -2)):
					if (str(self.chessboard[dest_row, dest_col], encoding='utf-8') != '   '):
						return 0
					elif(str(self.chessboard[dest_row + 1, dest_col], encoding='utf-8') != '   '):
						return 0
					else:
						return 1
			return 0

		if (str(self.chessboard[dest_row, dest_col], encoding='utf-8') != '   '):  
			if (self.pick_piece(str(self.chessboard[dest_row, dest_col], encoding='utf-8')).player == current_piece.player):
				return 0
		if (flag == 1):
			for (row, col) in path_of_move:
				if (str(self.chessboard[row, col], encoding='utf-8') != '   '):
					return 0
		return flag

	def get_totalscore(self, player): 
		#function to get score by summing up the scores of each piece
		total_score = 0
		temp = 1
		for piece in self.pieces:
			if(piece.player == player):
				temp = 1
			elif(piece.player != player):
				temp = -1
			total_score += temp * piece.score
		return  total_score

	def checkmate(self,current_player): 
		checkmate = 0
		if(current_player == 'W'): 
			king_piece = self.pick_piece('WK ')
		else:
			king_piece = self.pick_piece('BK ')
		if(king_piece == 0):
			return 1 
		kr, kc = king_piece.pos_index()
		check_move = 0
		escape_move = 0
		for new_row, new_col in [(kr,kc), (kr-2,kc), (kr+2,kc), (kr,kc-2), (kr,kc+2), (kr+2,kc+2),(kr-2,kc-2)]:
			if((new_row in range(self.shape[0])) and (new_col in range(self.shape[1]))): 
				if ((str(self.chessboard[new_row, new_col], encoding='utf-8') == '  ') or ((new_row,new_col) == (kr,kc))): 
					king_pos = pos_tostr(new_row,new_col)
					if(self.size == 'MiniSize'): 
						king_pos = columns[new_col] + str(4 - new_row)
					escape_move += 2
					for playing in self.pieces:
						if(playing.player != king_piece.player):
							if(self.possible_checkmateMove(playing,king_pos) == 1):
								check_move += 2
								break
		if((escape_move>0) and (check_move == escape_move)): 
			checkmate = 1 
		return checkmate

def pos_tostr(row,col): 
	#Numeric position to string position 
	pos0 = columns[col]
	pos1 = str(8-row)
	return pos0+pos1

def pos_toint(cell): 
	#String position to numeric position 
	col = columns.index(cell[0])
	row = 8 - int(cell[1])
	return (row, col)

class chessPieces():
	def __init__(self, pieceName, size):
		self.size = size # Standard or Minigame
		self.type = '' #Pawn, Rook, Bishop, King, Queen
		self.pieceName = pieceName #this should be a string such as 'BP1' for the first piece of Black Pawn
		self.initial_pos = '' #Initial position like A1
		self.moves = 0 #number of moves of the pices - to check if it has moved 

		#Positions of each piece on the board
		#Pawn
		if ((pieceName.startswith('BP'))or (pieceName.startswith('WP'))):
			self.type = 'Pawn'
			self.score = 20
			if (pieceName.startswith('W')):
				self.initial_pos = columns[int(pieceName[2]) - 1]+'2'
				if(size == 'MiniSize'):
					if(pieceName == 'WP1'):
						self.initial_pos = 'A1'
					elif(pieceName == 'WP2'):
						self.initial_pos = 'D1'
					elif(pieceName == 'WP3'):
						self.initial_pos = 'D1'
					elif(pieceName == 'WP4'):
						self.initial_pos = 'A1'
			else:
				self.initial_pos = columns[8 - int(pieceName[2])]+'7'
				if (size == 'MiniSize'):
					if (pieceName == 'BP1'):
						self.initial_pos = 'D4'
					elif (pieceName == 'BP2'):
						self.initial_pos = 'A4'
					elif(pieceName == 'BP3'):
						self.initial_pos = 'A4'
					elif(pieceName == 'BP4'):
						self.initial_pos = 'D4'
		#Rook
		elif ((pieceName.startswith('BR')) or (pieceName.startswith('WR'))):
			self.type = 'Rook'
			self.score = 60
			if (pieceName == 'WR1'):
				self.initial_pos = 'A1'
				if(size == 'MiniSize'):
					self.initial_pos = 'A1'
			elif (pieceName == 'WR2'):
				self.initial_pos = 'H1'
				if(size == 'MiniSize'):
					self.initial_pos = 'D1'
			elif (pieceName == 'WR3'):
				self.initial_pos = 'B1'
			elif (pieceName == 'WR4'):
				self.initial_pos = 'G1'
			elif (pieceName == 'BR1'):
				self.initial_pos = 'H8'
				if (size == 'MiniSize'):
					self.initial_pos = 'D4'
			elif (pieceName == 'BR2'):
				self.initial_pos = 'A8'
				if (size == 'MiniSize'):
					self.initial_pos = 'A4'
			elif (pieceName == 'BR3'):
				self.initial_pos = 'G8'
			elif (pieceName == 'BR4'):
				self.initial_pos = 'B8'
		#Bishop
		elif ((pieceName.startswith('BB')) or (pieceName.startswith('WB'))):
			self.type = 'Bishop'
			self.score = 50
			if (pieceName == 'WB1'):
				self.initial_pos = 'C1'
				if(size == 'MiniSize'):
					self.init_pos = 'A1'
			elif (pieceName == 'WB2'):
				self.initial_pos = 'F1'
				if (size == 'M'):
					self.init_pos = 'D1'
			elif (pieceName == 'BB1'):
				self.initial_pos = 'F8'
				if (size == 'MiniSize'):
					self.init_pos = 'D4'
			elif (pieceName == 'BB2'):
				self.initial_pos = 'C8'
				if (size == 'M'):
					self.init_pos = 'A4'
		#King
		elif (pieceName in ['WK ','BK ']):
			self.type = 'King'
			self.score = 150
			if(pieceName.startswith('W')):
				self.initial_pos = 'D1'
				if(size == 'MiniSize'):
					self.initial_pos = 'B1'
			else:
				self.initial_pos = 'D8'
				if(size == 'MiniSize'):
					self.initial_pos = 'B4'
		#Queen
		elif (pieceName in ['WQ ','BQ ']):
			self.type = 'Queen'
			self.score = 100
			if (pieceName.startswith('W')):
				self.initial_pos = 'E1'
				if(size == 'MiniSize'):
					self.initial_pos = 'C1'
			else:
				self.initial_pos = 'E8'
				if(size == 'MiniSize'):
					self.initial_pos = 'C4'

		self.current_pos = self.initial_pos
		self.player = pieceName[0]

	def pos_index(self): 
		#fuction to identify piece position such as  'D4' (on the chessboard) and convert to  a numeric index 
		if(self.size == 'MiniSize'): 
			col = columns.index(self.current_pos[0])
			row = 4 - int(self.current_pos[1])
			return (row,col)
		return pos_toint(self.current_pos) 

	def str_name(self):
		return self.pieceName

	def possible_moves(self, goal, capture):
		#function to specify all possible moves of a particular piece 
		path_of_move = []
		flag = 0 #to keep a check if a move is possible 
		destination_row, destination_col = pos_toint(goal)
		if(self.size == 'MiniSize'): 
			destination_col = columns.index(goal[0])
			destination_row = 4 - int(goal[1])
		source_row, source_col = self.pos_index()
		#Pawn
		#Each Pawn advances one square at a time except for the first move, it can have two steps 
		#Each Pawn can move diagonally to capture the opponent
		if(self.type == 'Pawn'): 
			if(capture == 1): 
				if(self.player == 'W'):
					if((destination_row - source_row) == -1):
						if(abs(source_col - destination_col) == 1):
							flag = 1
				if (self.player == 'B'):
					if ((destination_row - source_row) == 1):
						if (abs(source_col - destination_col) == 1):
							flag = 1
			else:
				if(self.moves == 0): 
					if (self.player == 'W'):
						if ((destination_row - source_row) in [-1,-2]):
							if (source_col - destination_col == 0):
								flag = 1
								path_of_move.append((source_row - 1, source_col))
								if(destination_row - source_row == -2):
									path_of_move.append((source_row - 2, source_col))
					if (self.player == 'B'):
						if ((destination_row - source_row) in [1,2]):
							if (source_col - destination_col == 0):
								flag = 1
								path_of_move.append((source_row + 1, source_col))
								if (destination_row - source_row == 2):
									path_of_move.append((source_row + 2, source_col))
				else:
					if (self.player == 'W'):
						if ((destination_row - source_row) == -1):
							if (source_col - destination_col == 0):
								flag = 1
					if (self.player == 'B'):
						if ((destination_row - source_row) == 1):
							if (source_col - destination_col == 0):
								flag = 1
		#Rook
		#Rook only moves in a straight horizontally/vertically  
		elif (self.type == 'Rook'): 
			move_row = abs(destination_row - source_row)
			move_col = abs(destination_col - source_col)
			if ((move_row + move_col > 0) and (move_row * move_col == 0)):
				flag = 1
				if (move_col == 0):
					if (destination_row - 1 > source_row):
						for i in range(source_row + 1, destination_row):
							path_of_move.append((i, source_col))
					elif (source_row - 1 > destination_row):
						for i in range(destination_row + 1, source_row):
							path_of_move.append((i, source_col))
				if (move_row == 0):
					if (destination_col - 1 > source_col):
						for j in range(source_col + 1, destination_col):
							path_of_move.append((source_row, j))
					elif (source_col - 1 > destination_col):
						for j in range(destination_col + 1, source_col):
							path_of_move.append((source_row, j))
		#Bishop
		#Bishop can only move diagonally 
		elif (self.type == 'Bishop'): 
			move_row = abs(destination_row - source_row)
			move_col = abs(destination_col - source_col)
			if (move_row == move_col):
				flag = 1
				dir_row = (destination_row - source_row) / move_row
				dir_col = (destination_col - source_col) / move_col
				row = source_row
				col = source_col
				while (1):
					row += dir_row
					col += dir_col
					if ((row == destination_row) or (col == destination_col)):
						break
					path_of_move.append((int(row), int(col)))
		#King
		#Kings moves 2 squares in a horizontally/vertically
		elif(self.type == 'King'): #King
			if (self.player == 'B'):
				if (((abs(destination_row - source_row) == 2) and (abs(source_col - destination_col) == 0)) or ((abs(destination_row - source_row) == 0) and (abs(source_col - destination_col) == 2 ))):
					flag = 1
			else:
				if (self.player == 'W'):
					if (((abs(destination_row - source_row) == 2) and (abs(source_col - destination_col) == 0)) or ((abs(destination_row - source_row) == 0) and (abs(source_col - destination_col) == 2 ))):
						flag = 1
		#Queen
		#Queen can move in any direction and take as many steps 
		elif (self.type == 'Queen'): 
			move_row = abs(destination_row - source_row)
			move_col = abs(destination_col - source_col)
			#horizontal/vetical moves
			if ((move_row + move_col > 0) and (move_row * move_col == 0)): 
				flag = 1
				if(move_col == 0):
					if(destination_row - 1 > source_row):
						for i in range(source_row+1,destination_row):
							path_of_move.append((i,source_col))
					elif(source_row - 1 > destination_row):
						for i in range(destination_row+1,source_row):
							path_of_move.append((i,source_col))
				if (move_row == 0):
					if (destination_col - 1 > source_col):
						for j in range(source_col + 1, destination_col):
							path_of_move.append((source_row,j))
					elif (source_col - 1 > destination_col):
						for j in range(destination_col + 1, source_col):
							path_of_move.append((source_row,j))
			#diagonal moves 
			if (move_row == move_col): 
				flag = 1
				rdir = (destination_row - source_row) / move_row
				cdir = (destination_col - source_col) / move_col
				row = source_row
				col = source_col
				while(1):
					row += rdir
					col += cdir
					if((row == destination_row) or (col == destination_col)):
						break
					path_of_move.append((int(row),int(col)))
					
		if(flag == 1): 
			#satisfying condition for a possible move
			self.current_pos = goal
			self.moves = 1
		return flag,path_of_move

	def RulesEnforced(self, goal): 
		#function to ensure rules are followed to fit possible move of a particular piece 
		flag = 0
		path_of_move = []
		destination_row, destination_col = pos_toint(goal)
		source_row, source_col = self.pos_index()
		if (self.size == 'MiniSize'):
			destination_col = columns.index(goal[0])
			destination_row = 4 - int(goal[1])

		if(self.type == 'Pawn'):
			if (self.player == 'W'):
				if ((destination_row - source_row) == -1):
					if (abs(source_col - destination_col) == 1):
						flag = 1
			if (self.player == 'B'):
				if ((destination_row - source_row) == 1):
					if (abs(source_col - destination_col) == 1):
						flag = 1

		elif (self.type == 'Rook'):
			move_row = abs(destination_row - source_row)
			move_col = abs(destination_col - source_col)
			if ((move_row + move_col > 0) and (move_row * move_col == 0)):
				flag = 1
				if (move_col == 0):
					if (destination_row - 1 > source_row):
						for i in range(source_row + 1, destination_row):
							path_of_move.append((i, source_col))
					elif (source_row - 1 > destination_row):
						for i in range(destination_row + 1, source_row):
							path_of_move.append((i, source_col))
				if (move_row == 0):
					if (destination_col - 1 > source_col):
						for j in range(source_col + 1, destination_col):
							path_of_move.append((source_row, j))
					elif (source_col - 1 > destination_col):
						for j in range(destination_col + 1, source_col):
							path_of_move.append((source_row, j))

		elif (self.type == 'Bishop'):
			move_row = abs(destination_row - source_row)
			move_col = abs(destination_col - source_col)
			if (move_row == move_col):
				flag = 1
				dir_row = (destination_row - source_row) / move_row
				dir_col = (destination_col - source_col) / move_col
				row = source_row
				col = source_col
				while (1):
					row += dir_row
					col += dir_col
					if ((row == destination_row) or (col == destination_col)):
						break
					path_of_move.append((int(row), int(col)))  

		elif(self.type == 'King'):
			if (self.player == 'B'):
				if (((abs(destination_row - source_row) == 2) and (abs(source_col - destination_col) == 0)) or ((abs(destination_row - source_row) == 0) and (abs(source_col - destination_col) == 2 ))):
					flag = 1
			else:
				if (self.player == 'W'):
					if (((abs(destination_row - source_row) == 2) and (abs(source_col - destination_col) == 0)) or ((abs(destination_row - source_row) == 0) and (abs(source_col - destination_col) == 2 ))):
						flag = 1

		elif (self.type == 'Queen'):
			move_row = abs(destination_row - source_row)
			move_col = abs(destination_col - source_col)
			if ((move_row + move_col > 0) and (move_row * move_col == 0)): 
				flag = 1
				if(move_col == 0):
					if(destination_row - 1 > source_row):
						for i in range(source_row+1,destination_row):
							path_of_move.append((i,source_col))
					elif(source_row - 1 > destination_row):
						for i in range(destination_row+1,source_row):
							path_of_move.append((i,source_col))
				if (move_row == 0):
					if (destination_col - 1 > source_col):
						for j in range(source_col + 1, destination_col):
							path_of_move.append((source_row,j))
					elif (source_col - 1 > destination_col):
						for j in range(destination_col + 1, source_col):
							path_of_move.append((source_row,j))
			if (move_row == move_col): 
				flag = 1
				dir_row = (destination_row - source_row) / move_row
				dir_col = (destination_col - source_col) / move_col
				row = source_row
				col = source_col
				while(1):
					row += dir_row
					col += dir_col
					if((row == destination_row) or (col == destination_col)):
						break
					path_of_move.append((int(row),int(col)))
		
		return flag,path_of_move 

def get_player_action(minichess, minitype): 
	#function to get the user inputs to position the pieces 
	game = chessboardState(minichess=minichess,minitype=minitype)
	turnmod = ['W', 'B']
	moving_player = ['White', 'Black']
	turn = 0
	while(turn < 50):
		turn += 1
		print('------- TURN ' + str(turn) + '-------')
		game.showChessBoard()
		print(moving_player[turn % 2]+' is making the move...')
		valid = 0
		while(valid == 0):
			print('Select one of the options to continue: 1.Make a move, 2.Quit the game') 
			option = input('Enter Choice ( 1 or 2): ')
			if (option == '1'): 
				#Make a move
				piece = input('Enter name of the piece you want to move( BP1, WP1 etc.,): ')
				if (game.pick_piece(piece) == 0): 
					#given list of pieces does not contain  such  a piece 
					print('Incorrect piece ')
					continue
				elif (game.pick_piece(piece).player != turnmod[turn % 2]): 
					#desired piece is of the opponent
					print('Incorrect piece ')
					continue
				else:
					goal = input('Enter the desired position to move the piece at ( A1, D4 etc.,): ')
					if (len(goal) != 2): 
						#format mismatch
						print('Invalid move ')
						continue
					elif ((goal[0] not in game.columns) or (goal[1] not in game.rows)): 
						#invalid position on the chessboard
						print('Invalid move ')
						continue
					else:
						flag = game.move_piece(piece, goal) 
						if (flag == 0): 
							print('Invalid move')
							continue
						else:
							valid = 1 #One turn is accomplished
			elif(option == '2'):
				#Quit the game
				print('XXXXXXX GAME OVER XXXXXXX') 
				return 0
			else:
				print('Invalid operation. ')
				continue
		if(game.checkmate(turnmod[(turn + 1) % 2]) == 1): #Check if there is a checkmate
			print('Winner of the game is : ' + moving_player[turn % 2] )
			break
		print(moving_player[turn % 2] + ' score is ', game.get_totalscore(moving_player[turn % 2]))
	print('XXXXXXX GAME OVER XXXXXXX')
	return 0



