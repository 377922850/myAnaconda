# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 22:17:45 2017

@author: fcy
"""

#condition = 1
#while condition < 10:
#    print(condition)
#    condition = condition + 1
#    print(condition)
    
#while True:
#    print('i am a student')

#print(1 == 1)

#a =range(10)
#print(a)

#while a:
#    print(a[-1])
#    a = a[:len(a)-1]
    
#example_list = [1,2,3,4,5,6,7,12,543,876,12,3,2,5]
#for i in example_list:
#    print(i)
    
#tup = ('python', 2.7, 64)
#for i in tup:
#    print(i)
    
#dic = {}
#dic['version'] = 2.7
#dic['lan'] = 'python'
#
#dic['platform'] = 64
#for key in dic:
#    print(key, dic[key])    
    
#s = set(['python', 'python2', 'python3','python'])
#for item in s:
#    print(item)


# define a Fib class
#class Fib(object):
#    def __init__(self, max):
#        self.max = max
#        self.n, self.a, self.b = 0, 0, 1
#
#    def __iter__(self):
#        return self
#
#    def __next__(self):
#        if self.n < self.max:
#            r = self.b
#            self.a, self.b = self.b, self.a + self.b
#            self.n = self.n + 1
#            return r
#        raise StopIteration()
#
## using Fib object
#for i in Fib(100):
#    print(i)
    
    
#def fib(max):
#    a, b = 0, 1
#    while max:
#        r = b
#        a, b = b, a+b
#        max -= 1
#        yield r
#
## using generator
#for i in fib(5):
#    print(i)
    
#x = 4
#y = 2
#z = 3
#if x > 1:
#    print ('x > 1')
#elif x < 1:
#    print('x < 1')
#else:
#    print('x = 1')
#print('finish')



#def sale_car(price, color='red', brand='carmy', is_second_hand=True):
#    print('price', price,'\n'
#          'color', color,'\n'
#          'brand', brand,'\n'
#          'is_second_hand', is_second_hand,)
#    
#    
#sale_car(1000)

#encoding=utf-8
#import jieba
#
#seg_list = jieba.cut("我来到北京清华大学",cut_all=True)
#print("Full Mode:", "/ ".join(seg_list)) #全模式
#
#seg_list = jieba.cut("我来到北京清华大学",cut_all=False)
#print("Default Mode:", "/ ".join(seg_list)) #精确模式
#
#seg_list = jieba.cut("他来到了网易杭研大厦") #默认是精确模式
#print(", ".join(seg_list))
#
#seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造") 
#print(", ".join(seg_list))



#text = "hei,my name is fcy"
#
#my_file_test_test = open('my_file_test_test.txt','w')
#my_file_test_test.write(text)
#my_file_test_test.close()

#text_append = '\nThis is appended file.'
#
#my_file_test_test = open('my_file_test_test.txt','w')
#my_file_test_test.write(text_append)
#my_file_test_test.close()

#text_append = '\nThis is appended file.'

#my_file_test_test = open('my_file_test_test.txt','r')
#content = my_file_test_test.readlines()
#print(content)
#for item in content:
#    print(item)


#class Calculator:
#    name = 'Good'
#    price = 18
#    def __init__(self,name,price,hight,width,weight):
#        self.name = name
#        self.price = price
#        self.hight = hight
#        self.wi = width
#        self.we = weight        
#    def add(self,x,y):
#        print(self.name)
#        result = x - y
#        print(result)
#    def minus(self,x,y):
#        result = x - y
#        print(result)
        

    
#a_input = int(input('please give me a number:\n'))
#if a_input == '1':
#    print('heihei')


#a = 1,2,3,4,5


#a = [1,2,3,4,5,6,7,8]
#
#a.insert(0,0)   # plsition value
#print(a)


#a = [1,2,3,4,2,6,7]
#a.remove(2)     # remove only the first appeared value
#print(a)

#a = [1,2,3,4,2,6,7]
#print(a[:-3])

#a = [1,2,3,4,2,6,7]
#b = a.index(2)
#print(b)

#a = [1,2,3,4,2,6,7]
#b = a.count(1)
#print(b)

#a = [1,2,3,4,2,6,7]
#a.sort(reverse=True)
#print(a)

#a = [1,2,3,4]
#multi_dim_a = [[1,2,3],
#               [4,5,6],
#               [5,6,7],
#               [5,6,7]]
#print(len(a))
#print(len(multi_dim_a))
#print(a[1])
#print(multi_dim_a[2][0])

#d = {'apple':1,'pear':2,'orange':3}
#print(d)
#print(d['apple'])
#del d['pear']
#print(d)
#d['a'] = 20
#print(d)
#k = {'apple':[1,2,3],'pear':{1:3,3:'a'}}
#print(k)
#print(k['apple'])
#print(k['apple'][2])

#from time import*
##from time import time,localtime
##import time as t
#print(localtime())
#print(time())


#"""
#A simple example for Reinforcement Learning using table lookup Q-learning method.
#An agent "o" is on the left of a 1 dimensional world, the treasure is on the rightmost location.
#Run this program and to see how the agent will improve its strategy of finding the treasure.
#View more on my tutorial page: https://morvanzhou.github.io/tutorials/
#"""
#
#import numpy as np
#import pandas as pd
#import time
#
#np.random.seed(2)  # reproducible
#
#
#N_STATES = 6   # the length of the 1 dimensional world
#ACTIONS = ['left', 'right']     # available actions
#EPSILON = 0.9   # greedy police
#ALPHA = 0.1     # learning rate
#GAMMA = 0.9    # discount factor
#MAX_EPISODES = 13   # maximum episodes
#FRESH_TIME = 0.003    # fresh time for one move
#
#
#def build_q_table(n_states, actions):
#    table = pd.DataFrame(
#        np.zeros((n_states, len(actions))),     # q_table initial values
#        columns=actions,    # actions's name
#    )
#    # print(table)    # show table
#    return table
#
#
#def choose_action(state, q_table):
#    # This is how to choose an action
#    state_actions = q_table.iloc[state, :]
#    if (np.random.uniform() > EPSILON) or (state_actions.all() == 0):  # act non-greedy or state-action have no value
#        action_name = np.random.choice(ACTIONS)
#    else:   # act greedy
#        action_name = state_actions.idxmax()    # replace argmax to idxmax as argmax means a different function in newer version of pandas
#    return action_name
#
#
#def get_env_feedback(S, A):
#    # This is how agent will interact with the environment
#    if A == 'right':    # move right
#        if S == N_STATES - 2:   # terminate
#            S_ = 'terminal'
#            R = 1
#        else:
#            S_ = S + 1
#            R = 0
#    else:   # move left
#        R = 0
#        if S == 0:
#            S_ = S  # reach the wall
#        else:
#            S_ = S - 1
#    return S_, R
#
#
#def update_env(S, episode, step_counter):
#    # This is how environment be updated
#    env_list = ['-']*(N_STATES-1) + ['T']   # '---------T' our environment
#    if S == 'terminal':
#        interaction = 'Episode %s: total_steps = %s' % (episode+1, step_counter)
#        print('\r{}'.format(interaction), end='')
#        time.sleep(2)
#        print('\r                                ', end='')
#    else:
#        env_list[S] = 'o'
#        interaction = ''.join(env_list)
#        print('\r{}'.format(interaction), end='')
#        time.sleep(FRESH_TIME)
#
#
#def rl():
#    # main part of RL loop
#    q_table = build_q_table(N_STATES, ACTIONS)
#    for episode in range(MAX_EPISODES):
#        step_counter = 0
#        S = 0
#        is_terminated = False
#        update_env(S, episode, step_counter)
#        while not is_terminated:
#
#            A = choose_action(S, q_table)
#            S_, R = get_env_feedback(S, A)  # take action & get next state and reward
#            q_predict = q_table.ix[S, A]
#            if S_ != 'terminal':
#                q_target = R + GAMMA * q_table.iloc[S_, :].max()   # next state is not terminal
#            else:
#                q_target = R     # next state is terminal
#                is_terminated = True    # terminate this episode
#
#            q_table.ix[S, A] += ALPHA * (q_target - q_predict)  # update
#            S = S_  # move to next state
#
#            update_env(S, episode, step_counter+1)
#            step_counter += 1
#    return q_table
#
#
#if __name__ == "__main__":
#    q_table = rl()
#    print('\r\nQ-table:\n')
#    print(q_table)



