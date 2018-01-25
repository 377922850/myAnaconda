# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 22:32:31 2018

@author: fcy
"""

#def function(a,b):
#    c = a*b
#    print('The c is',c)

#def fun1(price,is_second_hand,colour='red',brand='dazhong'):
#    print('price:',price,
#          'colour:',colour,
#          'brand:',brand,
#          'is_second:',is_second_hand,
#          )
#fun1(1000,'red')
#APPLE = 100
#a = 30
#def fun():    
#    global a
#    print(a)
#    return APPLE+a
#
#print(fun())
#print(a)

##text = 'This is my first line.\nThis is next line.'
#append_file = '\nThis is appended file'
##print(text)
##my_file = open('my_file.txt','w')   # w:write
#my_file = open('my_file.txt','a')    # a:append
#my_file.write(append_file)
#my_file.close()

#file = open('my_file.txt','r')
#content = file.readlines()   #line
#print(content)
#
#python_list = [1,2,3,4,5]

#class Calculate:
#    name = 'Good Calculate'
#    price = 18
#    def add(self,x,y):
#        result = x+y
#        print(result,'The name is',self.name)
#    def minus(self,x,y):
#        result = x-y
#        print(result)
#    def times(self,x,y):
#        result = x*y
#        print(result)
#    def divide(self,x,y):
#        result = x/y
#        print(result)

#a_input = input('Please input a number:')
#if a_input == '1':
#    print('heihei') 
#elif a_input == '2':   
#    print('11')

# =============================================================================
# # tuple 元祖   list 列表
# a_tuple = (12,3,4,5,6)
# another_tuple = 2,3,4,5,6,7,8
# a_list = [1,22,36,4,5]
# 
# #for content in a_list:
# #    print(content)
# #    
# #for content in another_tuple:
# #    print(content)
#     
# for index in range(len(a_list)):
#     print(index)
# =============================================================================


# =============================================================================
# a = [1,5,8,0,4,6,8]
# print(a)
# a.append(0)
# print(a)
# a.insert(0,100)
# print(a)
# a.remove(0)
# print(a[:3])
# 
# #会覆盖原有的list
# a.sort(reverse=True)  #倒叙
# print(a)
# =============================================================================


# =============================================================================
# #d = {'apple':1,'orange':3}
# #e = {1:2,3:5,'a':'c'}
# #print(d['apple'])
# #del d['orange']
# #print(d)
# #d['b']=20
# #print(d)
# #d['c']=1
# #print(d)
# import m1
# print(m1.data1())
# =============================================================================


# =============================================================================
# a = [(1,2),(2,4)]
# for i,j in a:
#     print(i,j)
#     
# fun2 = lambda x,y:x+y
# print(fun2(5,5))
# =============================================================================

# =============================================================================
# #copy   deepcopy
# import copy 
# a = [1,2,3]
# b = a
# print(id(a))
# print(id(b))
# b[0] = 11
# print(a)
# print(id(a))
# print(id(b))
# c = copy.copy(a)
# print(id(a) == id(c))
# print(a)
# c[0]=33
# print(c)
# 
# e=3
# f=e
# print(e)
# print(f)
# f=5
# print(id(f))
# print(id(e))
# print(e)
# =============================================================================


# =============================================================================
# import pickle
# #a_dict = {'da':111,2:[2,3,4],'23':{1:2,'d':'sad'}}
# #file = open('pickle_example.pickle','wb')
# #pickle.dump(a_dict,file)
# #file.close()
# 
# #file = open('pickle_example.pickle','rb')
# #a_dict = pickle.load(file)
# #file.close()
# #print(a_dict)
# with open('pickle_example.pickle','rb') as file:
#     a_dicit1 = pickle.load(file)
# =============================================================================
     
#char_list=['a','b','a','c','r','d']
#a = list(set(char_list))