
import matplotlib.pyplot as plt
from random import randint
from pylab import *

esquina=[(1,1),(2,3),(3,1)]


punto1= (randint(0,3),randint(0,3))
Mx = [2]
My = [2]
for i in range(50000):
    e=randint(0,3)
    punto2 = esquina[e]
    
    x = (punto2[0] + punto1[0]) / 2.0
    y = (punto2[1] + punto1[1]) / 2.0
    
    punto1 = (x,y)
    Mx.append(x)
    My.append(y)
    
#plt.ion()

plt.plot(Mx, My,'b.')