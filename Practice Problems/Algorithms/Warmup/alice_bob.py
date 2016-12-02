# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 01:53:53 2016

@author: user
"""

a0,a1,a2 = input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]
aliceList=[a0,a1,a2]
bobList=[b0,b1,b2]
alice=0;
bob=0;


for i in range(3):
    if(aliceList[i]>bobList[i]):
        alice+=1
    elif(aliceList[i]<bobList[i]):
        bob+=1
    
print(alice,bob)
    