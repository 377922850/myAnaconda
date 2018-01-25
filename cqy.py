# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 00:20:23 2017

@author: fcy
"""

import matplotlib.pyplot as plt  
from wordcloud import WordCloud  
import jieba  
from wordcloud import WordCloud, ImageColorGenerator  
import os  
import numpy as np  
import PIL.Image as Image  
  
newtext = []  
#打开F盘下的聊天记录文件e.txt  
for word in open('E:\myfile\robotmaster\873323430.txt', 'r',encoding='utf-8'):  
    tmp = word[0:4]  
    #print(tmp)  
    if (tmp == "2017" or tmp == "===="):#过滤掉聊天记录的时间和qq名称  
        continue  
    tmp = word[0:2]  
    #print(tmp)  
    if (tmp[0] == '[' or tmp[0] == '/'):#过滤掉图片和表情，例如[图片]，/可爱  
        continue  
    newtext.append(word)  
  
#将过滤掉图片和表情和时间信息和qq名称剩下的文字重新写入F盘下的ab.txt文件中去  
with open('D:\\a2.txt', 'w', encoding='utf-8') as f:  
    for i in newtext:  
        f.write(i)  
#打开新生成的聊天记录文件  
text = open('D:\\a2.txt', 'r',encoding = 'utf-8').read()  
word_jieba = jieba.cut(text, cut_all=True)  
word_split = " ".join(word_jieba)  
#找一张小黄人logo图来生成配色方案,小黄人logo图小黄人.jpg路径在F:\\盘下  
alice_coloring = np.array(Image.open(os.path.join('Alice.png')))  
my_wordcloud = WordCloud(background_color="white", max_words=2000, mask=alice_coloring,  
                         max_font_size=40, random_state=42,  
                         font_path='C:/Windows/Fonts/简体.ttf') 
#    .generate(word_split)  
image_colors = ImageColorGenerator(alice_coloring)  
plt.imshow(my_wordcloud.recolor(color_func=image_colors))  
plt.imshow(my_wordcloud)  
plt.axis("off")  
plt.show() 