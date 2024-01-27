# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 15:29:15 2024

@author: Я
"""

import random
import time
import math
print ('RandoMM_3.17K')
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
d=float(3.14237)
e=float(2.22579)
for i in range(2,200,2):
    f=random.randrange(0,100)
    g=random.randrange(0,200)
    h=math.sin(a*b*c*i)/d/i/math.pi
    k=math.cos(f/i/g)*d*e
    print(i,f,g,h,k)
    time.sleep(1)
print('End')
input()
