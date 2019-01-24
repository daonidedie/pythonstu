#!usr/bin/python
# -*- coding: utf-8 -*-

# Beautiful Soup 是一个可以从HTML或XML文件中提取数据的Python库。 
# 它能够通过你喜欢的转换器实现惯用的文档导航,查找,修改文档的方式。 
# 在爬虫开发中主要用的是Beautiful Soup的查找提取功能。 
# Beautiful Soup是第三方模块，需要额外下载 
# 下载命令：pip install bs4 
# 安装解析器：pip install lxml 

import urllib;
import re;
from bs4 import BeautifulSoup;



rep= urllib.urlopen("http://www.sohu.com").read();
#创建一个bs对象
#默认不指定的情况，bs会选择python内部的解析器
#因此指定lxml作为解析器
soup=BeautifulSoup(rep,"lxml");
for a in  soup.find_all("a"):

    print (a.attrs);

#print(rep);

print ("1212121");
fruits = ['banana', 'apple',  'mango'];
for index in range(len(fruits)):
    print '当前水果 :', fruits[index];
 
print "Good bye!";


print ("rsfds1111fsd");



#https://blog.csdn.net/qq_41841569/article/details/85929509
# 一件有趣的事：我用 Python 爬了爬自己的微信朋友
# 2019年01月06日 15:04:50 Python新世界 阅读数：5185
# 版权声明：禁止转载至其它平台，转载至博客需带上此文链接。	https://blog.csdn.net/qq_41841569/article/details/85929509
# 最近几天干啥都不来劲，昨晚偶然了解到Python里的itchat包，它已经完成了wechat的个人账号API接口，使爬取个人微信信息更加方便。
# 鉴于自己很早之前就想知道诸如自己微信好友性别比例都来自哪个城市之类的问题，于是乎玩心一起，打算爬一下自己的微信。
# 首先，在终端安装一下itchat包。
#  学习Python中有不明白推荐加入交流群
#                 号：960410445
#                 群里有志同道合的小伙伴，互帮互助，
#                 群里有不错的视频学习教程和PDF！
# pip install itchat
# 安装完成后导入包，再登陆自己的微信。过程中会生产一个登陆二维码，扫码之后即可登陆。登陆成功后，把自己好友的相关信息爬下来。