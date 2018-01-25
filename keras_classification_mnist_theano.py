# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 00:32:10 2017

@author: fcy
"""

import numpy as np
np.random.seed(1337)  # for reproducibility
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential #线性叠加模型
from keras.layers import Dense, Activation #Dense:full connection
from keras.optimizers import RMSprop

# download the mnist to the path '~/.keras/datasets/' if it is the first time to be called
# X shape (60,000 28x28), y shape (10,000, )
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# data pre_processing
X_train = X_train.reshape(X_train.shape[0], -1) / 255.   # normalize
X_test = X_test.reshape(X_test.shape[0], -1) / 255.      # normalize
y_train = np_utils.to_categorical(y_train, num_classes=10) # label process
y_test = np_utils.to_categorical(y_test, num_classes=10)  # label process

# build our neural net
model = Sequential([
        Dense(32,input_dim=784),
        Activation('relu'),
        Dense(10),
        Activation('softmax')
        ])
 
# define your optimizer
rmsprop = RMSprop(lr=0.0001,rho=0.9,epsilon=1e-08,decay=0.0)
# lr：大于0的浮点数，学习率
# rho：大于0的浮点数
# epsilon：大于0的小浮点数，防止除0错误

model.compile(
        optimizer=rmsprop,
        loss='categorical_crossentropy',
        metrics=['accuracy'],
        )
#optimizer：指定模型训练的优化器；
#loss：目标函数；
#class_mode: ”categorical”和”binary”中的一个，只是
#用来计算分类的精确度或using the predict_classes method


# training
print('Training......')
model.fit(X_train,y_train,epochs=2,batch_size=32)
#fit(X, y, batch_size=128, epochs=100, verbose=1, 
#    validation_split=0,validation_data=None,shuffle=True,
#    show_accuracy=False,callbacks=[],class_weight=Noe, 
#    sample_weight=None)
#X：训练数据
#y : 标签
#batch_size : 每次训练和梯度更新块的大小。
#epochs: 迭代次数。
#verbose : 进度表示方式。0表示不显示数据，1表示显示进度条，2表示用只显示一个数据。
#callbacks : 回调函数列表。就是函数执行完后自动调用的函数列表。
#validation_split : 验证数据的使用比例。
#validation_data : 被用来作为验证数据的(X, y)元组。会代替validation_split所划分的验证数据。
#shuffle : 类型为boolean或 str(‘batch’)。是否对每一次迭代的样本进行shuffle操作（可以参见博文Theano学习笔记01--Dimshuffle()函数）。’batch’是一个用于处理HDF5（keras用于存储权值的数据格式）数据的特殊选项。
#show_accuracy:每次迭代是否显示分类准确度。

# testing
print('\nTesting......')
loss,accuracy = model.evaluate(X_test,y_test)
#evalute(X, y, batch_size=, 
#        show_accuracy=False,verbose=1, sample_weight=None)
#返回：误差率或者是(误差率，准确率)元组（if show_accuracy=True）
#参数：和fit函数中的参数基本一致，其中verbose取1或0，表示有进度条或没有

print('test loss:',loss)
print('test accuracy:',accuracy)