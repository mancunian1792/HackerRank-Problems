# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 02:42:24 2016

@author: user
"""

import sys


num=int(input())
border=input().strip().split(' ');
m,hmin,hmax=input().strip().split(' ');

hmin=int(hmin)
start=int(border[0]);
end=int(border[len(border)-1]);

print(start-hmin);


