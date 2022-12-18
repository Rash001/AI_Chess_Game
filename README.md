# AI_Chess_Game

# GAME OF CHESS (using Artificial Intelligence)

## Helper functions

<br>[Chess Board Setup & Rules Enforced] (https://github.com/Rash001/AI_Chess_Game/blob/main/ChessboardState.py) 
<br>[MiniMax Tree Evaluation] (https://github.com/Rash001/AI_Chess_Game/blob/main/chessMiniMax.py)

## Execute:
[To Start the execution] (https://github.com/Rash001/AI_Chess_Game/blob/main/playChess.py)


## Dependencies 
import numpy 
install using the command : pip install numpy

import matplotlib
install using the command : pip install matplotlib

## To Start Playing the Game
Python playChess.py

## Steps To Execute 

The first move is played by the AI
Step 1: Press 'Enter' to see the move
Step 2: Now give an input in the for of x,y (eg. 6,0) indicating  position of the piece you need to move
Step 3: Now give an input in the for of x,y (eg. 5,0) indicating  the position  on the board where you would like your piece to move 
Step 4: Continue this until checkmate(either of the king has been killed)
Find the color of the player piece (Black/White) displayed as the winner with a score of each player by the end of the game

## Histogram Plots 
![Scores](https://github.com/Rash001/AI_Chess_Game/blob/main/ScoresAs_in_Report.png)
![FiveStatesAIvsAI](https://github.com/Rash001/AI_Chess_Game/blob/main/StatesGameAs_in_report.png)

## Steps for Execution 
1. Run the file playChess.py
2. Select an option either a (1 or 2) if you select 1:
    a) Choice 1 lets you choose players the board size ( 1 throgh 5)
    b) Then you are prompted to choose two players ( such as Tree Based AI, Baseline AI or Human)
    c) You are prompted to pick an option between making a move or quit the game ( 1 or 2)
        i) Make a move? -> Piece Name ( should be enterened as BP1, WP1)
        ii) Quit? -> Output presents as Game Over!
3.  Select an option either a (1 or 2) if you select 2:
    a) Choice 2 lets you get Tree Based AI model to compete with Baseline AI model
    a) You are promted to enter iterations ( number of games ) you want the AIs to compete at all five defined states 
    b) The output will show a list of scores with winners of each game anf two histograms and one bar graph 


## Citations and Attributions

<br>(https://towardsdatascience.com/train-your-own-chess-ai-66b9ca8d71e4)
<br>(https://www.geeksforgeeks.org/game-playing-in-artificial-intelligence/)
<br>(https://github.com/luweizhang/chess-ai/blob/master/chessgame.py)
<br>Russell, Stuart J., et al. “The Minimax Search Algorithm.” Artificial Intelligence: A Modern Approach, Fourth Edition, Fourth ed., Pearson Education, Harlow, 2021, pp. 146–151. 
<br>Dirk94.“Dirk94/Chessai: Chess Ai Written in Python. GitHub, https://github.com/Dirk94/ChessAI. 
<br>“Minimax Algorithm in Game Theory: Set 1 (Introduction).” GeeksforGeeks, 13 June 2022, https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/. 
<br>“NumPy Documentation#.” NumPy Documentation - NumPy v1.23 Manual, https://numpy.org/doc/stable/. 
<br>“Copy in Python (Deep Copy and Shallow Copy).” GeeksforGeeks, 12 Oct. 2022, https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/. 
<br>“Histograms#.” Histograms - Matplotlib 3.6.2 Documentation, https://matplotlib.org/stable/gallery/statistics/hist.html. 
<br>“Numpy.random.randint#.” Numpy.random.randint - NumPy v1.23 Manual, https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html
<br>Eppes, Marissa. “How a Computerized Chess Opponent ‘Thinks’ - the Minimax Algorithm.” Medium, Towards Data Science, 6 Oct. 2019, https://towardsdatascience.com/how-a-chess-playing-computer-thinks-about-its-next-move-8f028bd0e7b1. 
