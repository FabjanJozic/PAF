import numpy as np
import matplotlib.pyplot as plt
import math

import calculus as cal                  #type: ignore


def funkcija(x):
    return x**2 + 1

x1 = 1
x2 = 9
y = []

gornja_suma = []
donja_suma = []
trapez = []
raspon = []
for br in np.arange(10, 1000, 10):
    y.append(((x2**3)/3+x2) - ((x1**3)/3+x1))
    raspon.append(br)
    gornja_suma.append(cal.integral_square(funkcija, x1, x2, br)[0])
    donja_suma.append(cal.integral_square(funkcija, x1, x2, br)[1])
    trapez.append(cal.integral_trapezoid(funkcija, x1, x2, br))


fig = plt.figure(figsize=(12,6.2), dpi=100)
axes = fig.add_axes([0.15, 0.15, 0.75, 0.75])
plt.rcParams.update({'font.size': 8})           #type: ignore
axes.plot(raspon, gornja_suma, 'b',marker='o', markersize=3, markerfacecolor="blue")      
axes.plot(raspon, donja_suma, 'r', marker='o', markersize=3, markerfacecolor="red")      
axes.plot(raspon, trapez, 'g', marker='o', markersize=3, markerfacecolor="green") 
axes.plot(raspon, y, 'k')      
axes.set_xlabel('broj podjela za numeričku integraciju')           
axes.set_ylabel('')                 
axes.grid(lw=0.5)                    
axes.legend(['gornja integralna suma postupkom pravokutnika', 'donja integralna suma postupkom pravokutnika',
             'integralna suma postupkom trapeza', 'analitička vrijednost integracije'], loc='best')              

plt.show()

