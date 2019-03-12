#!usr/bin/python
# -*- coding: utf-8 -*-
import urllib;

numbers =[12,23,3434,4534,34,534,5,345,23,432,4,234,2];
even=[];
odd=[]
while(len(numbers))>0:
    numb= numbers.pop();
    if(numb%5==0):
        even.append(numb);
    else:
        odd.append(numb);

print even;
print odd;
      




