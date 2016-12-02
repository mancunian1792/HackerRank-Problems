# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 22:05:31 2016

@author: user
"""

#!/bin/python3

import sys
import math


def check_prime(n):
    flag =0;
    for i in range(2,int(math.sqrt(n))+1):
        #print("I is ",i)
        if(n % i == 0):
            flag =1;
            break;
    
    if(flag == 1):
        #print("N is Non Prime:::",n)
        return -1
    else:
        #print("N is Prime:::",n)
        return 1


start,stop = input().strip().split(' ')
start,stop = [int(start),int(stop)]
counter=0;
for i in range(start,stop+1):
    #Check if is prime or not !
    if(check_prime(i) == 1):
        if(check_prime(i+2) == 1):
            
            #print(i,i+2)
            counter=counter+1;

print(counter)