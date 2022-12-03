import chessboard
import chessPieces
import pieceMoves
import chessMiniMax
import tabulate
from tabulate import tabulate



def get_player_action(state): #function to get the user inputs to position the pieces 
	board, player = state
	current_move = input('Enter the  indicies of the piece you want move ( x,y -> x is row and y is column)')
	new_move = input('Enter the  indicies of target position move you want move ( x,y -> x is row and y is column)')
	current = tuple(map(int, current_move.split(',')))
	new = tuple(map(int, new_move.split(',')))
	return  current, new

if __name__ == '__main__': #Main Function

    game = chessboard.ChessBoard()
    print("Let the game begin!!")
    print(end = '\n')
    print( "Initial state of the board: ")
    game.showChessBoard() 
    player = "white"
    AI_Player = "black"
    scoreAI = 0
    scoreP = 0
    print( "All States Possible: ")
    print(end = '\n')
    print(tabulate(chessMiniMax.ChessMinimax.possible_states(game.chessboard, player)))
    state = game.chessboard,player
    while not chessboard.ChessBoard.game_over(game):
        print("AI's Turn")
        input("Press Enter to continue...")
        root = chessMiniMax.ChessMinimax.create_minimax_tree(game, game.chessboard, player)
        scoreAI += chessMiniMax.ChessMinimax.evaluation(game.chessboard,player)
        game.chessboard = chessMiniMax.ChessMinimax.minimax(root, 0, True, -99999,99999,"black").data
        game.showChessBoard() 

        print("Player's Turn")
        cur,new = get_player_action(state)
        game.chessboard = pieceMoves.RulesEnforced.move_piece(game.chessboard, cur, new)
        scoreP += chessMiniMax.ChessMinimax.evaluation(game.chessboard,player)
        game.showChessBoard()

    if game.winner != "none":
        print("Winner of the game is ",game.winner)  
        print('Score of the Human Player is :', scoreP ) 
        print('Score of the AI Player is :', scoreAI ) 
    