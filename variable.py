# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 23:53:37 2017

@author: fcy
"""

import tensorflow as tf
state = tf.Variable(0,name='counter')
print(state.name)
one = tf.constant(1)

new_value = tf.add(state , one)
update = tf.assign(state,new_value)

init = tf.initialize_all_variables() # must have if define variable

#sess = tf.Session()
#sess.run(init)
#
#sess.run(update)
#print(sess.run(state))
#sess.run(update)
#print(sess.run(state))
#sess.run(update)
#print(sess.run(state))
#sess.close()

with tf.Session() as sess:
    sess.run(init)
    for step in range(3):
        sess.run(update)
        print(sess.run(state))