# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 23:47:15 2016

@author: user
"""

#!/bin/python3

import sys
import math


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
count =0;


#Square matrix conditions - Handled below
if(n==m ):
    if(n%2 == 0):
        print("1st condition")
        print(int((n*m)/4));
    else:
        print("1st else condition")
        count=int(((n-1)*(m-1))/4)+2*int(math.floor(n/2))+1
        print(count); 

        
#Number of rows greater than columns 
elif((n>m) & (n%2 == 0)):
    if(m%2 == 0):
        print("2nd condition")
        print(int((n*m)/4));
    else:
        print("2nd else condition")
        count=int((n*(m-1))/4)+int(math.floor(n/2))
        print(count);
elif((n>m) & (n%2 !=0)):
    if(m%2 ==0):
        #print("2nd elif condition")
        count=int(((n-1)*m)/4)+int(math.floor(m/2))
        print(count);
    else:
        #print("2nd elif else condition")
        count=int((n-1)*(m-1)/4)+int(math.floor(m/2))+int(math.floor(n/2))+1
        print(count);

        
# Number of Columns greater than rows
elif((n<m) & (m%2 ==0)):
    if(n%2==0):
        print("3rd condition")
        print(int((n*m)/4));
    else:
        print("3rd else condition")
        count=int(((n-1)*m)/4)+int(math.floor(m/2))
        print(count);
elif((n<m) & (m%2 !=0)):
    if(n%2==0):
        print("3rd elif condition")
        count=int((n*(m-1))/4)+int(math.floor(n/2))
        print(count);
    else:
        print("3rd elif else condition")
        count=int((n-1)*(m-1)/4)+int(math.floor(m/2))+int(math.floor(n/2))+1
        print(count)