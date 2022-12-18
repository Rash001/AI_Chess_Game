from optparse import Option
import ChessboardState
import chessMiniMax
import numpy as np
import random as rd
import copy

def Game_user_action(minichess, game_size): #Initiate a real game
    color = 'B'     #For convenience, AIs always move first
    while(1):
        print('Please select two players in the game: ')
        print(' 1.Tree Based AI, 2.Baseline AI, 3.Manually')
        player1 = input('Select Player 1: ')
        player2 = input('Select Player 2: ')
        if((player1 in ['1', '2', '3']) and (player2 in ['1', '2', '3'])):
            player1 = int(player1)
            player2 = int(player2)
            if((player1 == player2) and (player1 == 3)): 
                #Human vs Human game
                ChessboardState.get_player_action(minichess,game_size)
                return 0
            elif((player1 != 3) and (player2 != 3)): 
                #AI vs AI game
                select_AIvsAI_game(game_size, player1, player2)
                return 0
            else:
                #AI vs Human game
                for player in [player1, player2]:
                    if(player != 3):
                        AI_player = player
                        break
                # chessMiniMax.AI_based_game(minichess,game_size, AI_player)
                # return 0
                if (AI_player == 1):
                    new_game = ChessboardState.chessboardState(minichess=minichess, minitype=game_size)
                    AI_Game = chessMiniMax.Tree_BasedAI(new_game, color)
                if (AI_player == 2):
                    new_game = ChessboardState.chessboardState(minichess=minichess, minitype=game_size)
                    AI_Game = chessMiniMax.Random_AI(new_game, color)
            break
        else:
            print('Entered value is invalid ')
    turn = 0
    turnmod = ['W', 'B']
    moving_piece = ['White', 'Black']
    AI_role = 1
    while (turn < 40):
        turn += 1
        print('------- TURN ' + str(turn) + '-------')
        AI_Game.show_state()
        print(moving_piece[turn % 2]+ ' is making the move...')
        if (moving_piece[turn % 2] == moving_piece[AI_role]):
            if(player1 == 1):
                AI_Game.create_minimax_tree()
            else:
                AI_Game.create_move_option()
            valid = 1
        else:
            valid = 0
        while (valid == 0 ):
            print('Select one of the options to continue: 1.Make a move, 2.Quit the game')  
            option = input('Enter Choice ( 1 or 2)')
            if (option == '1'):
                piece = input('Enter name of the piece you want to move( BP1, WP1 etc.,): ')
                if (AI_Game.pick_piece(piece) == 0):  # No such piece in the current list of pieces
                    print('Incorrect piece ')
                    continue
                elif (AI_Game.pick_piece(piece).player != turnmod[turn % 2]):  # The piece belongs to the opponent
                    print('Incorrect piece ')
                    continue
                else:
                    goal = input('Enter the desired position to move the piece at ( A1, D4 etc.,):')
                    if (len(goal) != 2):  # Incorrect format
                        print('Invalid move ')
                        continue
                    elif ((goal[0] not in AI_Game.AI.state.columns) or (goal[1] not in AI_Game.AI.state.rows)): 
                        print('Invalid move ')
                        continue
                    else:
                        successful = AI_Game.AI.state.move_piece(piece, goal) 
                        #print('Success', successful) 
                        if (successful == 0):  # Move cannot be done
                            print('Invalid move ')
                            continue
                        else:
                            valid = 1  # One turn is accomplished
            elif (option == '2'):
                print('XXXXXXX GAME OVER XXXXXXX')  # Quit the game
                return 0
            else:
                print('Entered value is invalid')
                continue
        if (AI_Game.checkmate(turnmod[(turn + 1) % 2]) == 1):  # Check if there is a checkmate
            print(moving_piece[turn % 2] + ' Wins the game! ')
            break
    print('XXXXXXX GAME OVER XXXXXXX')
    return 0


def select_AIvsAI_game(problem_size, AI1, AI2): 
    #AI vs AI
    if (problem_size == 1):
        minichess = 'False'  # 8*8 game
    else:
        minichess = 'True'  # 4*4 game
    new_game = ChessboardState.chessboardState(minichess=minichess, minitype=problem_size)
    if(AI1 == 1):
        player1 = chessMiniMax.Tree_BasedAI(new_game, 'B')
        print('Black: TreeAI')
    else:
        player1 = chessMiniMax.Random_AI(new_game, 'B')
        print('Black: BaselineAI')
    if (AI2 == 1):
        player2 = chessMiniMax.Tree_BasedAI(new_game, 'W')
        print('White: TreeAI')
    else:
        player2 = chessMiniMax.Random_AI(new_game, 'W')
        print('White: BaselineAI')
    turn = 0
    while (turn >= 0):
        print('------- TURN ' + str(turn) + '-------')
        if (turn % 2 == 0):
            if(AI1 == 1):
                player1.create_minimax_tree()
                new_state = player1.AI.state
                player2.update_new_state(new_state) 
            else:
                player1.create_move_option()
                new_state = player1.AI.state
                player2.update_new_state(new_state)
        else:
            if(AI2 == 1):
                player2.create_minimax_tree()
                new_state = player2.AI.state
                player1.update_new_state(new_state)
            else:
                player2.create_move_option()
                new_state = player2.AI.state
                player1.update_new_state(new_state)
        key = input("Enter any key to continue ... ('Use Q or q to quit the game!')")
        if( key == 'Q' or key == 'q' ):
            print("XXXXXXX GAME OVER XXXXXXX")
            return 0
        else:
            pass
        new_state.showChessBoard()
        turn += 1
        if (player1.checkmate('B') == 1):  
            #white wins
            current_state = player1.AI.state
            print('White wins the game!')
            break
        if (player2.checkmate('W') == 1):  
            #black wins
            print('Black wins the game!')
            break
        if (turn == 40):  
            current_state = player1.AI.state
            if (current_state.get_totalscore('W') > current_state.get_totalscore('B')):
                print('White wins the game! ') 
            elif (current_state.get_totalscore('W') < current_state.get_totalscore('B')):
                print('Black wins the game! ')
            else:
                print('Draw! ')
            break

if __name__ == '__main__':
    print(end = '\n')
    print("WELCOME TO THE GAME OF CHESS!!")
    print(end = '\n')
    x = input('Enter your choice of execution (1 or 2 ( for 5 states AIvsAI execution )) :')
    if (int(x) == 1):
        while (1):
            game_size = input('Enter Game Size: '+ '\n' + '1.Standard Chess Game, 2.Minichess Game State_A, 3.Minichess Game State_B , 4.Minichess Game State_C, 5.Minichess Game State_D : ') 
                #enter 1, 2, 3 , 4 or 5
            if (game_size == '1'):  
                Game_user_action('False', int(game_size))
                break
            elif (game_size in ['2','3','4','5']):  
                Game_user_action('True', int(game_size))
                break
            else:
                print('Entered value is invalid')
                continue
    else:
    #Tree_Based_AI & Baseline 5 instances  ( you could give n = 100 or any numeric value )
        n = input( 'Number of iterations:' )
        chessMiniMax.AIvsAI_game(int(n))
        exit()
