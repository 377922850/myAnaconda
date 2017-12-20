# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 11:20:48 2017

@author: fcy
"""

from fcy_reinforcementlearning_example_RLbrain import QLearningTable 
from fcy_reinforcementlearning_example_enbironment import FCY 

def update():
    for episode in range(100):
        # initial observation
        observation = env.render()
        
        while True:    
            # RL choose action based on observation
            action = RL.choose_action(str(observation))
            
            # RL take action and get next observation and reward
            observation_, reward, done = env.step(action)
            
            # Rl learn from the transition
            RL.learn(str(observation), action, reward, str(observation_))
            
            # swap observation
            observation = observation_
            
            # break while loop when end of this episode
            if done:
                break
            
    # end of game
    print('game over')
    env.destroy()

if __name__ == "__main__":
    env = FCY()
    RL = QLearningTable(actions=list(range(env.n_actions)))

    env.after(100, update)
    env.mainloop()
            