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

## Steps for Execution 
1. Run the file playChess.py
2. Select an option either a (1 or 2) if you select 1:
    - Choice 1 lets you choose players the board size ( 1 throgh 5)
    - Then you are prompted to choose two players ( such as Tree Based AI, Baseline AI or Human)
    - You are prompted to pick an option between making a move or quit the game ( 1 or 2)
        - Make a move? -> Piece Name ( should be enterened as BP1, WP1)
        - Quit? -> Output presents as Game Over!
3.  Select an option either a (1 or 2) if you select 2:
    - Choice 2 lets you get Tree Based AI model to compete with Baseline AI model
    - You are promted to enter iterations ( number of games ) you want the AIs to compete at all five defined states 
    - The output will show a list of scores with winners of each game anf two histograms and one bar graph 

## Histogram Plots 
![Scores](https://github.com/Rash001/AI_Chess_Game/blob/main/ScoresAs_in_Report.png)
![FiveStatesAIvsAI](https://github.com/Rash001/AI_Chess_Game/blob/main/StatesGameAs_in_report.png)


## Citations and Attributions

<br>Spears, Logan. “Train Your Own Chess Ai.” Medium, Towards Data Science, 17 Aug. 2021, https://towardsdatascience.com/train-your-own-chess-ai-66b9ca8d71e4. 
<br>Russell, Stuart J., et al. “The Minimax Search Algorithm.” Artificial Intelligence: A Modern Approach, Fourth Edition, Fourth ed., Pearson Education, Harlow, 2021, pp. 146–151.</br> 
<br>Dirk94.“Dirk94/Chessai: Chess Ai Written in Python. GitHub, https://github.com/Dirk94/ChessAI. 
<br>“Minimax Algorithm in Game Theory: Set 1 (Introduction).” GeeksforGeeks, 13 June 2022, https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/. 
<br>“NumPy Documentation#.” NumPy Documentation - NumPy v1.23 Manual, https://numpy.org/doc/stable/. 
<br>“Copy in Python (Deep Copy and Shallow Copy).” GeeksforGeeks, 12 Oct. 2022, https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/. 
<br>“Histograms#.” Histograms - Matplotlib 3.6.2 Documentation, https://matplotlib.org/stable/gallery/statistics/hist.html. 
<br>“Numpy.random.randint#.” Numpy.random.randint - NumPy v1.23 Manual, https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html
<br>Eppes, Marissa. “How a Computerized Chess Opponent ‘Thinks’ - the Minimax Algorithm.” Medium, Towards Data Science, 6 Oct. 2019, https://towardsdatascience.com/how-a-chess-playing-computer-thinks-about-its-next-move-8f028bd0e7b1. 
<br>Luweizhang. “Chess-Ai/Chessgame.py at Master · Luweizhang/Chess-AI.” GitHub, https://github.com/luweizhang/chess-ai/blob/master/chessgame.py. 
