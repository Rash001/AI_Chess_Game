import re
import chessboard
import chessPieces
import copy
from typing import DefaultDict

class RulesEnforced():

	def piece_moves(board, player):
		#function to get the moves of each piece 
		piece_moves = DefaultDict() #this was added to avoid TypeError: 'type' object is not subscriptable
		pattern = player+'+'
		for i in range(0,8):
			for j in range(0,8):
				if(re.match(pattern, board[i][j])):
					if('Pawn' in board[i][j]):
						possible_moves = chessPieces.Pawn.possible_moves(board,[i,j])
					if('Rook' in board[i][j]):
						possible_moves = chessPieces.Rook.possible_moves(board,[i,j])
					if('Bishop' in board[i][j]):
						possible_moves = chessPieces.Bishop.possible_moves(board,[i,j])
					if('King' in board[i][j]):
						possible_moves = chessPieces.King.possible_moves(board,[i,j])
					if('Queen' in board[i][j]):
						possible_moves = chessPieces.Queen.possible_moves(board,[i,j])
					if possible_moves:
						piece_moves[(i,j)] = possible_moves
		return piece_moves

	def possible_moves_onBoard(current_pos, board):
		#function to return all possible moves of a particular piece from the current position on the board
		possible_moves = []
		if('Pawn' in board[current_pos[0]] [current_pos[1]]):
			possible_moves = chessPieces.Pawn.possible_moves(board, [current_pos[0], current_pos[1]])
		if('Rook' in board[current_pos[0]] [current_pos[1]]):
			possible_moves = chessPieces.Rook.possible_moves(board, [current_pos[0], current_pos[1]])
		if('Bishop' in board[current_pos[0]] [current_pos[1]]):
			possible_moves = chessPieces.Bishop.possible_moves(board, [current_pos[0], current_pos[1]])
		if('King' in board[current_pos[0]] [current_pos[1]]):
			possible_moves = chessPieces.King.possible_moves(board, [current_pos[0], current_pos[1]])
		if('Queen' in board[current_pos[0]] [current_pos[1]]):
			possible_moves = chessPieces.Queen.possible_moves(board, [current_pos[0], current_pos[1]])
		return possible_moves


	def move_piece(board,cur_pos, new_pos):
		chessboard = copy.deepcopy(board)
		if(new_pos[0] >= 0 and new_pos[0] < 8 and new_pos[1] >=0 and new_pos[1] < 8):
			piece = chessboard[cur_pos[0]][cur_pos[1]]
			chessboard[new_pos[0]][new_pos[1]] =  piece
			chessboard[cur_pos[0]][cur_pos[1]] = "     X     "
		return chessboard
