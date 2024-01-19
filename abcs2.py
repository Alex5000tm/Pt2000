# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 16:59:49 2024

@author: Я
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 14:58:54 2024

@author: Я
"""


import datetime

dt_now = datetime.datetime.now()
print(dt_now)

import math
a= float(input ('a='))
b= float(input ('b='))
c=float(math.cos(a)*math.cos(b))
print (c)
d=float(math.cos(c)*math.sin(c)/math.pi)
print (d)
e=float(math.sin(d)/c*math.pi)
print (e)
f=float(math.pi/math.cos(e))
print (f)
g=float(abs(d/e/f/math.pi))
print (g)
h=float(abs(d+e+f+g+c))
print (h)
input()
print ('next...')
t=float(input('t='))
k=float(input('k='))
q=float(d*e*f/g/h)*(math.cos(k)/math.sin(t)/math.pi)
print (q)
print ('End')
input ('Press Enter for quit...')
