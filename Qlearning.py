# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 22:33:47 2017

@author: fcy
"""

# =============================================================================
# Q learning
# Initialize Q arbitrarily //随机初始化Q值
# Repeat (for each episode): //每一次游戏，从小鸟出生到死亡是一个episode
#     Initialize S //小鸟刚开始飞，S为初始位置的状态
#     Repeat (for each step of episode):
#     根据当前Q和位置S，使用一种策略，得到动作A，这个策略可以是ε-greedy等
#     做了动作A，到达新的位置S'，并获得奖励R 
#     Q(S,A) ← Q(S,A) + α*[R + γ*maxQ(S',A') - Q(S,A)] //在Q中更新S
#     S ← S'
#     until S is terminal 
# =============================================================================
    
import numpy as np
import pandas as pd
import time

np.random.seed(2) # reproduciable:faker random number

N_STATES = 6 # the length of the one dimensional world 1维世界的宽度
ACTIONS = ['left','right'] # available actions 探索者的可用动作
EPSILON = 0.9 # greedy police 贪婪度
ALPHA = 0.1 # learning rate 学习率
GAMMA  = 0.9 # discount factor 奖励系数
MAX_EPISODES = 13 # max episoders 最大回合数
FRESH_TIME = 0.3 # fresh time for one mover 移动间隔时间

def build_q_table(n_states,actions):
    table = pd.DataFrame(
            np.zeros((n_states,len(actions))), # q table initial values
            columns = actions, # actions's name
    )
    print(table) # show table
    return table

build_q_table(N_STATES, ACTIONS) # test q table

def choose_action(state, q_table): # state:当前状态 q_table：q表
    # this is how to choose an action
    state_actions = q_table.iloc[state, :]
     # 非贪婪 or 或者这个state还没有探索过
    if(np.random.uniform()> EPSILON) or (state_actions.all() == 0):
        action_name = np.random.choice(ACTIONS)
    else: # act greedy
        action_name = state_actions.argmax()
    return action_name

def get_env_feedback(S,A):
    # this is how agent will interact with the environment 
    if A == 'right':
        if S == N_STATES - 2: # terminate S == 4
            S_ = 'terminal'
            R = 1
        else:
            S_ = S + 1
            R = 0
    else: # move left
        R = 0
        if S == 0:
            S_ = S
        else:
            S_ = S - 1
    return S_, R

def update_env(S, episode, step_counter):
    # This is how environment be updated
    env_list = ['-']*(N_STATES-1) + ['T']   # '---------T' our environment
    if S == 'terminal':
        interaction = 'Episode %s: total_steps = %s' % (episode+1, step_counter)
        print('\r{}'.format(interaction), end='')
        time.sleep(2)
        print('\r                                ', end='')
    else:
        env_list[S] = 'o'
        interaction = ''.join(env_list)
        print('\r{}'.format(interaction), end='')
        time.sleep(FRESH_TIME)   

# Q(S,A) ← Q(S,A) + α*[R + γ*maxQ(S',A') - Q(S,A)]   
def rl():
    # main part of RL loop
    q_table = build_q_table(N_STATES, ACTIONS)
    for episode in range(MAX_EPISODES):
        step_counter = 0
        S = 0
        is_terminated = False
        update_env(S, episode, step_counter)
        while not is_terminated:
            A = choose_action(S, q_table) # A:'left' or 'right'
            S_, R = get_env_feedback(S, A) # S:current S_:next R:reward
            q_predict = q_table.ix[S, A]
            if S_ != 'terminal':
                q_target = R + GAMMA * q_table.iloc[S_ ,:].max()
            else:
                q_target = R # next state is terminal
                is_terminated = True # terminate this episode
            # q_table Q(S,A) update    
            q_table.ix[S, A] += ALPHA * (q_target - q_predict)  
            S = S_  # move to state

            update_env(S, episode, step_counter+1) # update environment
            step_counter += 1
    return q_table                
  
if __name__ == "__main__":
    q_table = rl()
    print('\r\nQ-table:\n')
    print(q_table)    