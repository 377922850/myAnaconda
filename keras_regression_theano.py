# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 23:37:29 2017

@author: fcy
"""
#import os
#os.environ['KERAS_BACKEND']='theano'
import numpy as np
np.random.seed(1337)
from keras.models import Sequential
from keras.layers import Dense # full connection
import matplotlib.pyplot as plt

# create some data
X = np.linspace(-1,1,200)
# numpy.random.normal(loc=0.0, scale=1.0, size=None) 
# loc:Average probability distribution
# scale:Standard deviation of probability distribution
np.random.shuffle(X) # randomize the data
Y = 0.5*X + 2 + np.random.normal(0,0.05,(200,))
# plot data
plt.scatter(X,Y)
plt.show()

X_train,Y_train = X[:160],Y[:160] #the first 160 data
X_test,Y_test = X[160:],Y[160:] #the last 40 data

# build a nerual network from the 1st layer to the last layer
model = Sequential()
model.add(Dense(output_dim=1,input_dim=1))

# choose loss function and optimizing method
model.compile(loss='mse',optimizer='sgd') # mse均方误差 sgd随机梯度下降法

# training
print('Training......')
for step in range(301):
    cost = model.train_on_batch(X_train,Y_train)
    if step % 100 == 0:
        print('train cost',cost)
        
# testing
print('\nTesting')
cost = model.evaluate(X_test,Y_test,batch_size=40)
print('test cost',cost)
W,b = model.layers[0].get_weights()
print('Weights=',W,'\nBias=',b)

Y_pred = model.predict(X_test)
plt.scatter(X_test, Y_test)
plt.plot(X_test, Y_pred)
plt.show()

