# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 16:46:34 2016

@author: user
"""

nb=input();
for i in range(int(nb)):
    str=input();
    input1=str.split();
    #print(str[0]+":"+str[2]+":"+str[4]+":"+str[6]);
    x1=int(str[0]);
    y1=int(str[2]);
    x2=int(str[4]);
    y2=int(str[6]);
    
    xDiff=x2-x1;
    yDiff=y2-y1;
    newX=x2+xDiff;
    newY=y2+yDiff;
    print(newX,newY)
