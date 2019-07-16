# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 10:02:16 2019

@author: admin
"""

box=5
print("there are now", box, " bars in the box")

box = 5+5
print(box)

box=box+5
print(box)

#to describe dark, milk, and white chocolate bars 
D = "dark"
M = "milk"
W ="white"

print(D)
print(D, M, W)

def greeting(a):
    print("hello", a)
    
greeting("annie")

import math
dir(math)

math.pi
math.sqrt(16)
math.factorial(5)
math.factorial(0)
math.acos((math.pi)/2)
math.remainder(10,7)
math.pow(3,2)

def cubicroot(a):
    cubicroot = a**(1/3)
    print("the cubic root of", a, "is", cubicroot)
    
cubicroot(8)
cubicroot(math.pi)
cubicroot(115)
math.pow(27, 1/3)

print("please enter a value for x")
x=27
cubicroot(x)
