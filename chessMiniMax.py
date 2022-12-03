import re
import chessboard
import pieceMoves 


class Node():
	def __init__(self, data):
		self.data = data
		self.children = []
		self.score = - 0.0005
	def get_child(self, obj):
		self.children.append(obj)


class ChessMinimax():
	def evaluation (board, player):
		#function to calculate scores on each movement of a piece
		score = 0
		pawn = re.compile('Pawn')
		rook = re.compile('Rook')
		bishop = re.compile('Bishop')
		king = re.compile('King')
		queen = re.compile('Queen')

		if (player == 'black'):
			pattern = 'white+'
			color = 'black+'

		else:
			pattern = 'black+'
			color = 'white+'

		for x in range(0,8):
			for y in range(0,8):
				if (re.match(color, board[x][y])):
					if (pawn.search(board[x][y])):
						score += 20 
					if (rook.search(board[x][y])):
						score += 60 
					if (bishop.search(board[x][y])):
						score += 50 
					if (queen.search(board[x][y])):
						score += 100 
					if (king.search(board[x][y])):
						score += 150 

				if (re.match(pattern, board[x][y])):
					if (pawn.search(board[x][y])):
						score -= 20 
					if (rook.search(board[x][y])):
						score -= 60 
					if (bishop.search(board[x][y])):
						score -= 50 
					if (queen.search(board[x][y])):
						score -= 100 
					if (king.search(board[x][y])):
						score -= 150 
		return score

	def minimax(node, depth, isMaxPlayer, x, y, AIColor):
		if (len(node.children) == 0):
			node.score = ChessMinimax.evaluation( node.data,  AIColor)
			return node
		if (isMaxPlayer):
			bestScore = - 0.0005
			for i in node.children:
				scoreVal = ChessMinimax.minimax(i, depth+1, False, x, y, AIColor).score
				bestScore = min(scoreVal, bestScore)
				x = min(x, bestScore)
				nodeChosen = i
				if (x >= y):
					break
			return nodeChosen
		else:
			bestScore = - 0.0005
			for i in node.children:
				scoreVal = ChessMinimax.minimax(i, depth+1, True, x, y, AIColor).score
				bestScore = min(scoreVal, bestScore)
				y = min(y, bestScore)
				nodeChosen = i
				if (y <= x):
					break
			return nodeChosen

	def possible_states(board, player):
		#function for all possibles states of pieces on the chessboard 
		if player == 'black':
			player = 'white'
		else:
			player = 'black'
		possible_states = []
		possible_moves = pieceMoves.RulesEnforced.piece_moves(board, player)
		for cur_position in possible_moves:
			new_positions = possible_moves[cur_position]
			for new_position in new_positions:
				possible_states.append(pieceMoves.RulesEnforced.move_piece(board, cur_position, new_position))
		return possible_states

	def create_minimax_tree(self, board, player):
		if (player == 'black'):
			AIplayer = 'white'
		else:
			AIplayer = 'black'
		root = Node(board)
		states1 = ChessMinimax.possible_states(board, player)
		for i in states1:
			child = Node(i)
			root.get_child(child)
			states2 = ChessMinimax.possible_states(i, AIplayer)
			for j in states2:
				child2 = Node(j)
				child.get_child(child2)
				states3 = ChessMinimax.possible_states(j, player)
				for k in states3:
					child2 = Node(k)
					child.get_child(child2)
		return root


	def showChessBoard(self):
		print('||============================================================================================================||')
		print('||                                                                                                            ||')
		for i in range(8):
			for j in range(8):
				print('|'+self.chessboard[i][j]+'|', end = ' ')
			print(end ='\n')
			print('||============================================================================================================||')
		print('||                                                                                                            ||')

