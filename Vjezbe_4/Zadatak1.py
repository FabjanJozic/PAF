import matplotlib.pyplot as plt
import numpy as np

import calculus as cal              #type: ignore




def kubna(x):
    return x**3 +7

def sinus(x):
    return np.sin(x)

x = np.linspace(-3, 3, 300)
y_kubna_d = []
y_sinus_d = []
for i in range(len(x)):
    y_kubna_d.append(3*x[i]**2)
    y_sinus_d.append(np.cos(x[i]))

e1 = 0.5
e2 = 0.001

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(11, 7.2), dpi=100)
plt.rcParams.update({'font.size': 8})           #type: ignore
plt.axis('equal')
fig.tight_layout()
axes[0].plot(x, cal.derivation(kubna, x, e1, 3), 'b',marker='o', markersize=2, markerfacecolor="blue")      #type: ignore
axes[0].plot(x, cal.derivation(kubna, x, e2, 3), 'r', marker='o', markersize=2, markerfacecolor="red")      #type: ignore
axes[0].plot(x, y_kubna_d, 'k')               #type: ignore
axes[0].set_xlabel('x')                 #type: ignore
axes[0].set_ylabel('y')                 #type: ignore
axes[0].axis('tight')                   #type: ignore
axes[0].grid(lw=0.5)                    #type: ignore
axes[0].legend(['Vrijednost derivirane funkcije kada je dx {}.'.format(e1), 'Vrijednost derivirane funkcije kada je dx {}.'.format(e2),       #type: ignore
                'Analitička vrijednost derivacije funkcije.'], loc='best')              
axes[1].plot(x, cal.derivation(sinus, x, e1, 3), 'b', marker='o', markersize=2, markerfacecolor="blue")           #type: ignore
axes[1].plot(x, cal.derivation(sinus, x, e2, 3), 'r', marker='o', markersize=2, markerfacecolor="red")          #type: ignore
axes[1].plot(x, y_sinus_d, 'k')                #type: ignore
axes[1].set_xlabel('x')                 #type: ignore
axes[1].set_ylabel('y')                 #type: ignore
axes[1].axis('equal')                   #type: ignore
axes[1].grid(lw=0.5)                    #type: ignore
axes[1].legend(['Vrijednost derivirane funkcije kada je dx {}.'.format(e1), 'Vrijednost derivirane funkcije kada je dx {}.'.format(e2),       #type: ignore
                'Analitička vrijednost derivacije funkcije.'], loc='best') 
plt.show()