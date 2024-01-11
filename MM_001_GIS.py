# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 17:57:56 2024

@author: Я
"""

import math
import time
print ('Math_8.11')
print ('Enter data:__')
a=float(input('a= '))
b=float(input('b= '))
c=float(input('c= '))
print('Processing...')
for i in range (0, 110,10):
    x=math.cos(a*b*c)*i
    y=math.sin(a*b*c)*i
    z=math.cos(a*b*c)/math.sin(a*b*c)/(i+math.pi)
    time.sleep(1)
    print (x,y,z)
print ('Completed...')
time.sleep(2)
print ('End')
input ('Press Enter for exit...')
