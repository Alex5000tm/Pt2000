# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 12:16:49 2024

@author: Я
"""

from math import cos,sin,sqrt,pi
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
d=cos(a)*cos(b)*cos(c)
e=sin(a*b*c)+sqrt(d)/pi
print (d,e)
input()
