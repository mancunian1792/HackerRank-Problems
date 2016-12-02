# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 02:15:00 2016

@author: user
"""

#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
p_diag=0;
off_diag=0

for i in range(n):
    p_diag+=int(a[i][i])
    off_diag+=int(a[(n-1)-i][i])
print(abs(p_diag-off_diag))