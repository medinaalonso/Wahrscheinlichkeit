# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 23:25:21 2019

@author: AlonsoMC
"""

import random 
from collections import Counter 
import matplotlib.pyplot as plt

min=1
maxim=int(input("De cauntas caras quieres tu dado?"))
rolls=[random.randint(1,maxim) for i in range(100000)]
#print(rolls)
nms=Counter(rolls)
print(nms)
x=sorted(nms.items())

key=[lis[0] for lis in x]
res=[lis[1] for lis in x]
plt.bar(key,res)
plt.show()
