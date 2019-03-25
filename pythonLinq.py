#!usr/bin/python
# -*- coding: utf-8 -*-

#Linq 
#https://pypi.org/project/asq/
 
import random
from asq import query;
  
abc= ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
#print(query);
print query(abc).order_by(len).then_by().take(5).select(str.upper).to_list()
#打印长度大于3的所有值 sfds
for item in  query(abc).where(lambda p: len(p)>3).to_list():
     print item  



