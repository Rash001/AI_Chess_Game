import numpy as np 
import matplotlib.pyplot as plt 

#Scores of each game played ( Future Scope to dynamically add scores to list and plot )  

x = ['Game 1','Game 2','Game 3','Game 4','Game 5','Game 6','Game 7','Game 8']
AI_Player = [150, 250, 50 , -70, 1300, 150, 400, 50]
Human_Player = [350, 450, -50, 40, 1600, 50, 350, -50]
  
x_axis = np.arange(len(x))
  
plt.bar(x_axis - 0.2, AI_Player, 0.5, label = 'AI_Player')
plt.bar(x_axis + 0.2, Human_Player, 0.5, label = 'Human_Player')
  
plt.xticks(x_axis, x)
plt.xlabel("Games")
plt.ylabel("Scores")
plt.title("Game Score for each Player")
plt.legend()
plt.show()