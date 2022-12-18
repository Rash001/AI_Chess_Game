from sys import flags
import ChessboardState
import numpy as np
import random as rd
import copy
import matplotlib.pyplot as plt
 

# This class represents the AI player which uses the minimax algorithm to make the best move
class Node():
    def __init__(self, chess_state, player_color):
        self.state = chess_state
        self.player = player_color
        self.score = 0 #score of a particular node in Minimax algorithm
        self.children = []
        self.moves = (0,0) #(Piece, Goal, 0) parent node moving to the current node
   
    def current_scoreVal(self):
        #to get the score at current state
        return self.state.get_totalscore(self.player)
 
    # This function creates the tree of possible moves for the AI
    def chess_minimax(self, nplayer):
        # If the node is a leaf node, return the score
        if(len(self.children) == 0):
            self.score = self.current_scoreVal()
        # Iterate children and find the best score
        else:
            candidate_nodes = []
            for child in self.children:
                candidate_nodes.append(child.chess_minimax(nplayer))
            if (self.player == nplayer):
                self.score = max(candidate_nodes)
            else:
                self.score = min(candidate_nodes)
        return self.score



    def possible_states(self):
        node_list = []
        for piece in self.state.pieces:
            if (piece.player == self.player):
                for row in self.state.rows:
                    for col in self.state.columns:
                        if(col+row != piece.current_pos):
                            if(self.state.possible_checkmateMoveAI(piece,col+row) == 1):
                                node_list.append((piece.pieceName,col+row))
        return node_list
 
    def copy(self):
        return Node(chess_state = self.state, player_color = self.player)
 
    def evaluation(self, direction):
        temp = copy.deepcopy(self.state)
        temp.move_piece(direction[0],direction[1])
        return temp.get_totalscore(self.player)
   
    def new_state(self, nstate):
        self.state = nstate
 
def opponent_piece(player):
    if(player == 'W'):
        return 'B'
    if(player == 'B'):
        return 'W'
 
class Tree_BasedAI():
    def __init__(self, chess_state, player_color):
        self.AI = Node(chess_state,player_color)
 
   
    def create_minimax_tree(self):
        temp_AI = copy.deepcopy(self.AI)
        #copying the root node
        nodes_list = [[temp_AI]]
        node_count = 1
        max_depth = 2
        i = 0
        while(i < max_depth):
            current_nodes = nodes_list[i]
            new_nodes = []
            for node in current_nodes:
                current_piece = node.player
                possible_states = node.possible_states()
                for ps in possible_states:
                    current_state = copy.deepcopy(node.state)
                    current_state.move_piece(ps[0], ps[1])
                    new_AI = Node(chess_state=current_state, player_color=opponent_piece(current_piece))
                    new_AI.moves = ps
                    node.children.append(copy.copy(new_AI))
                    new_nodes.append(copy.copy(new_AI))
            nodes_list.append(new_nodes)
            node_count += len(new_nodes)
            i += 1
 
        print('The tree contains  ' + str(node_count) + ' nodes to process')
        sideAI = temp_AI.player
        total_score = nodes_list[0][0].chess_minimax(sideAI)
        candidates = []
        for child in nodes_list[0][0].children:
            if(child.score == total_score):
                candidates.append(child)
        if (len(candidates) == 1):
            chosen_node = candidates[0].moves
        else:
            rd.shuffle(candidates)
            chosen_node = candidates[0].moves
        print(chosen_node)
        self.AI.state.move_piece(chosen_node[0], chosen_node[1])
        return node_count
 
    def pick_piece(self, goal):
        return self.AI.state.pick_piece(goal)
 
    def checkmate(self, playing):
        king_piece = playing + 'K'
        if(self.pick_piece(king_piece) == 0):
            return 1
        else:
            return 0
   
    def update_new_state (self, new_state):
        self.AI.new_state(new_state)
 
    def show_state(self):
        self.AI.state.showChessBoard()
 
class Random_AI():
    def __init__(self, chess_state, player_color):
        self.AI = Node(chess_state,player_color)
 
    def pick_piece(self,goal):
        return self.AI.state.pick_piece(goal)
 
    def create_move_option(self):
        possible_states = self.AI.possible_states()
        rd.shuffle(possible_states)
        for chosen_state in possible_states:
            chosen = chosen_state
        try:
            print(chosen)
        except:
            chosen = possible_states[0]
        self.AI.state.move_piece(chosen[0],chosen[1])
 
    def checkmate(self,playing):
        king_piece = playing + 'K'
        if (self.pick_piece(king_piece) == 0):
            return 1
        else:
            return 0
   
    def update_new_state (self, new_state):
            self.AI.new_state(new_state)
 
    def show_state(self):
        self.AI.state.showChessBoard()
 

def AI_based_game(minichess, number, player):
    #AI vs Human
    player_color = ''
    if(player == '1'):
        player_color = 'B'
    elif(player == '2'):
        player_color = 'W'
    while(1):
        AI_select = input('Enter the AI you want as an opponent: 1.Tree Based, 2.Random Choice')
        if (AI_select == '1'):
            new_game = ChessboardState.chessboardState(minichess=minichess, minitype=number)
            AI_Game = Tree_BasedAI(new_game, player_color)
            break
        elif (AI_select == '2'):
            new_game = ChessboardState.chessboardState(minichess=minichess, minitype=number)
            AI_Game = Random_AI(new_game,player_color)
            break
        else:
            print('Invalid operation. ')
    turnmod = ['W', 'B']
    moving_piece = ['White', 'Black']
    turn = 0
    AI_play = int(player) - 1
    while (turn < 30):
        turn += 1
        print('------- TURN ' + str(turn) + '-------')
        AI_Game.show_state()
        print(moving_piece[turn % 2]+' is making the move...')
        if (moving_piece[turn % 2] == moving_piece[AI_play]):
            AI_Game.create_minimax_tree()
            valid = 1
        else:
            valid = 0
        while (valid == 0):
            print('Select one of the options to continue: 1.Make a move, 2.Quit the game')
            option = input('Enter Choice ( 1 or 2): ')
            if (option == '1'):
                piece = input('Enter name of the piece you want to move( BP1, WP1 etc.,): ')
                if (AI_Game.pick_piece(piece) == 0):  
                    #given list of pieces does not contain  such  a piece
                    print('Incorrect piece ')
                    continue
                elif (AI_Game.pick_piece(piece).player != turnmod[turn % 2]):
                    #desired piece is of the opponent  
                    print('Incorrect piece ')
                    continue
                else:
                    goal = input('Enter the desired position to move the piece at ( A1, D4 etc.,): ')
                    if (len(goal) != 2):  
                        #format mismatch
                        print('Invalid move ')
                        continue
                    elif ((goal[0] not in AI_Game.AI.state.column) or (goal[1] not in AI_Game.AI.state.row)):
                        #invalid position on the chessboard
                        print('Invalid move ')
                        continue
                    else:
                        flag = AI_Game.AI.state.move_piece(piece, goal)  
                        if (flag == 0):  
                            print('Invalid move ')
                            continue
                        else:
                            valid = 1  # One turn is accomplished
            elif (option == '2'):
                print('XXXXXXX GAME OVER XXXXXXX')
                return 0
           
            else:
                print('Invalid operation. ')
                continue
        if (AI_Game.checkmate(turnmod[(turn + 1) % 2]) == 1):  # Check if there is a checkmate
            print (moving_piece[turn % 2] + ' Wins the game! ')
            break
    print('XXXXXXX GAME OVER XXXXXXX')
    return 0
 
def AIvsAI_game(iterations):
    #Tree based AI vs Baseline AI
    Black_wins= [0,0,0,0,0]
    White_wins = [0,0,0,0,0]
    Tied_games = [0,0,0,0,0]
    Total_Win_Score = []
 
    #Iterate through all the problem sizes
    for problem_size in [1,2,3,4,5]:
        winners_list = []
        winners_scores = {'W' : [], 'B' : []}
        #Iterate through all the games
        for game in range(iterations):
            # Create a new game
            if (problem_size == 1):
                mini_select = 'False'
            else:
                mini_select = 'True'
            new_game = ChessboardState.chessboardState(minichess=mini_select, minitype=problem_size)
            player1 = Random_AI(new_game, 'W')
            player2 = Tree_BasedAI(new_game, 'B')
            turn = 0
            node_counts = []
 
            #Iterate through all the turns
            while (turn >= 0):
                print(problem_size,turn,winners_list)
                #Player 1's turn
                if (turn % 2 == 0):
                    player1.create_move_option()
                    new_state = player1.AI.state
                    player2.update_new_state(new_state)
                #Player 2's turn
                else:
                    node_count = player2.create_minimax_tree()
                    new_state = player2.AI.state
                    player1.update_new_state(new_state)
                    node_counts.append(node_count)
                #Check if there is a checkmate for player 1
                if(player1.checkmate('B') == 1):
                    winners_list.append('W')
                    winners_scores['W'].append(player1.AI.state.get_totalscore('W'))
                    winners_scores['B'].append(player1.AI.state.get_totalscore('B'))
                    Total_Win_Score.append(player2.AI.state.get_totalscore('W'))
                    White_wins[problem_size - 1] += 1
                   
                    break
                #Check if there is a checkmate for player 2
                if(player2.checkmate('W') == 1):
                    winners_list.append('B')
                    winners_scores['W'].append(player1.AI.state.get_totalscore('W'))
                    winners_scores['B'].append(player1.AI.state.get_totalscore('B'))
                    Total_Win_Score.append(player2.AI.state.get_totalscore('B'))
                    Black_wins[problem_size - 1] += 1
                    break
                #Check who wins the game, or else if it is a tie
                if(turn == 40):
                    current_state = player1.AI.state
                    if(current_state.get_totalscore('W') > current_state.get_totalscore('B')):
                        winners_list.append('W')
                        Total_Win_Score.append(current_state.get_totalscore('W'))
                        winners_scores['W'].append(current_state.get_totalscore('W'))
                        winners_scores['B'].append(current_state.get_totalscore('B'))
 
                        #print('Total Score of the Winner = ', Total_Win_Score)
                        White_wins[problem_size - 1] += 1
                    elif(current_state.get_totalscore('W') < current_state.get_totalscore('B')):
                        winners_list.append('B')
                        Total_Win_Score.append(current_state.get_totalscore('B'))
                        Black_wins[problem_size - 1] += 1
                        winners_scores['W'].append(current_state.get_totalscore('W'))
                        winners_scores['B'].append(current_state.get_totalscore('B'))
 
                    else:
                        winners_list.append('Tie')
                        Total_Win_Score.append(current_state.get_totalscore('B'))
                        Tied_games[problem_size - 1] += 1
                        winners_scores['W'].append(current_state.get_totalscore('W'))
                        winners_scores['B'].append(current_state.get_totalscore('B'))
                    break
                # Print Current Chess Board and go to next turn
 
                new_state.showChessBoard()
                turn += 1
           
            print('Total Score of winners: ', Total_Win_Score)
        print("Winner Sequence : ", winners_list)
        print("Winner Scores : ", winners_scores)
 
    f = plt.figure(1)
    x_labels = ['State 1', 'State 2', 'State 3', 'State 4', 'State 5']
    bar_width = 0.2
    temp_1 = np.arange(len(White_wins))
    temp_2 = temp_1 + bar_width
    temp_3 = temp_2 + bar_width
    plt.bar(temp_1, height=White_wins, width=bar_width, color='red', label='Baseline Wins')
    plt.bar(temp_2, height=Black_wins, width=bar_width, color='green', label='Tree Wins')
    plt.bar(temp_3, height=Tied_games, width=bar_width, color='blue', label='Draw')
    plt.ylim(0, iterations)
    plt.ylabel('Winning numbers')
    plt.xlabel('Problem sizes')
    plt.title("Winners in games played at each state")
    plt.legend(loc='upper right')
    plt.xticks(temp_2, x_labels)
    f.savefig('./Wins_FiveStatesGraph.png')
 
    g = plt.figure(2)
    plt.hist(White_wins, bins = 10, alpha = 0.5, label = 'Baseline')
    plt.hist(Black_wins, bins = 10, alpha = 0.5, label = 'Minimax')
    plt.hist(Tied_games, bins = 10, alpha = 0.5, label = 'Tied')
    plt.legend(loc = 'upper right')
    g.savefig('./Hist_Wins_FiveStatesGraph.png')
 
    print("BaseLine/White wins: ", White_wins)
    print("MinMaxTreeAI/Black wins: ", Black_wins)
    print("Tied games: ", Tied_games)
 
    h = plt.figure(3)
    plt.hist(node_counts, bins=10)
    plt.xlabel("Instances of nodes")
    plt.ylabel("Count of nodes")
    plt.title("Histogram of Possible nodes for every move in a game")
    h.savefig('./Score_MiniMaxChessGraph.png')
 
 