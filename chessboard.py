import chessPieces
import pieceMoves

class ChessBoard():
#creating an 8x8 chessboard

	def __init__ (self):
		self.chessboard = [["     X     "] * 8 for c in range (0, 8)]

		#chess pieces 
		#1. Pawns
		for p in range(0, 8):
			self.chessboard[1][p] = ' blackPawn '
			self.chessboard[6][p] = ' whitePawn '

		#2. Rooks
		self.chessboard[0][0] = ' blackRook '
		self.chessboard[0][2] = ' blackRook '
		self.chessboard[0][5] = ' blackRook '
		self.chessboard[0][7] = ' blackRook '
		self.chessboard[7][0] = ' whiteRook '
		self.chessboard[7][2] = ' whiteRook '
		self.chessboard[7][7] = ' whiteRook '
		self.chessboard[7][5] = ' whiteRook '
		
		#3. Bishops
		self.chessboard[0][1] = 'blackBishop'
		self.chessboard[0][6] = 'blackBishop'
		self.chessboard[7][1] = 'whiteBishop'
		self.chessboard[7][6] = 'whiteBishop'
		
		#4. Kings 
		self.chessboard[7][3] = 'whiteQueen '
		self.chessboard[0][4] = 'blackKing  '

		#5. Queens
		self.chessboard[0][3] = 'blackQueen '
		self.chessboard[7][4] = 'whiteKing  '

		self.current_player = "b"
		self.winner = "none"

	def game_over(game):
		#Function that counts the number of kings at every instant in the game and if there is just a single king remaining game is over
		game_over = False
		countking = 0
		kings = []
		for i in range (0,8):
			for j in range (0,8):
				if 'King' in game.chessboard[i][j]:
					countking += 1
					kings.append(game.chessboard[i][j])
		if countking == 1:
			game_over = True
			if 'black' in kings[0]:
				game.winner = 'Black'
			else:
				game.winner = 'White'
		return game_over

	def game_tied(chessboard):
		#function for when only two kings remain or there are no more moves 
		print("The Game is a Tied!")
		return False

	def winner(chessboard):
		winner = ''
		return winner

	def showChessBoard(self):
		print('||============================================================================================================||')
		print('||                                                                                                            ||')
		for i in range(8):
			for j in range(8):
				print('|'+self.chessboard[i][j]+'|', end = ' ')
			print(end ='\n')
			print('||============================================================================================================||')
		print('||                                                                                                            ||')