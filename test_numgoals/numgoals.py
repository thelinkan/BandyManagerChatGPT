from numpy import random as rand
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

#penguins = sns.load_dataset("penguins")

#print(penguins)







num_games = 3000

#home_off = 5000
#home_def = 4000
#away_off = 3000
#away_def = 3500

#home_off_part = home_off/away_def
#away_off_part = away_off/home_def

num_goals_2 = rand.poisson(2,num_games)
num_goals_3 = rand.poisson(3,num_games)

df = pd.DataFrame(num_goals_2)
df['l30'] = pd.DataFrame(num_goals_3)
print(df)
#print("home")
#rint(num_goals_home)
#print("away")
#print(num_goals_away)

sns.displot(data=df)
plt.show
