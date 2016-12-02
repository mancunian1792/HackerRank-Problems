# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 03:05:42 2016

@author: user
Best divisor
"""

#!/bin/python3

import sys




def factors(n):
    return set(x for tup in ([i, n//i] 
                for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

n = int(input().strip())
factor=factors(n);
sumDigits=[];
var=1;
for i in factor:
    sumDigits.append(sum_digits(i));
    var+=1
sumDigits.sort();
print(sumDigits[len(sumDigits)-1])



