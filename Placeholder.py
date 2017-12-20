# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 00:20:25 2017

@author: fcy
"""
import tensorflow as tf

input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)

output = tf.multiply(input1,input2)

with tf.Session() as sess:
    print(sess.run(output,feed_dict={input1:[7.],input2:[2.]}))