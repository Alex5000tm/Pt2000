# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 16:06:29 2024

@author: Я
"""

import math
import time
import os
a=float (input('a= '))
b=float (input('b= '))
c=float (input('c= '))
d=float (input('d= '))
time_1= float(input('time= '))
for i in range (0,110,10):
    x=math.cos(a*b*c/d)*time_1*i
    y=math.sin(a*b*c/d)/time_1*i
    z=math.sqrt(a*b*c/d)/time_1*i
    time.sleep(1)
    print (x,y,z)
print('End')
time.sleep(20)
input('Press any key...')
os.system('cls')
input('Press Enter for exit...')
