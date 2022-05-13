import projectile as pro                                    #type: ignore
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker



mass = 4.8
velocity = 21
alpha = 45
x0 = 0
y0 = 0
resistivity_constant = 0.32
surface_area = 1.08
air_density = 1.3
dt = 0.01

p = pro.Projectile()


M = []
range_M = []
Cd = []
range_Cd = []

for m in np.arange(0.5, 50.5, 0.5):
    M.append(m)
    p.set_initial_conditions(m, velocity, alpha, x0, y0)
    p.set_parameters(resistivity_constant, surface_area, air_density)
    range_M.append(p.range_RK4(dt))
    p.reset()
    
for c in np.arange(0, 1.1, 0.1):
    Cd.append(c)
    p.set_initial_conditions(mass, velocity, alpha, x0, y0)
    p.set_parameters(c, surface_area, air_density)
    range_Cd.append(p.range_RK4(dt))
    p.reset()
    
    
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 6), dpi=80)
plt.rcParams.update({'font.size': 8})                           #type: ignore
plt.axis('equal')
plt.subplots_adjust(wspace=0.4, hspace=0.9)
axes[0].plot(M, range_M, 'y')                                   #type: ignore
axes[0].set_xlabel('mass   $[kg]$')                             #type: ignore
axes[0].set_ylabel('range   $[m]$')                             #type: ignore
axes[0].grid(lw=0.5)                                            #type: ignore
axes[0].xaxis.set_major_locator(ticker.MultipleLocator(5))      #type: ignore
axes[0].axis('tight')                                           #type: ignore
axes[0].set_title('Ovisnost dometa o masi projektila')          #type: ignore
axes[1].plot(Cd, range_Cd, 'r')                                 #type: ignore
axes[1].set_xlabel('air resistivity constant')                  #type: ignore
axes[1].set_ylabel('range   $[m]$')                             #type: ignore
axes[1].grid(lw=0.5)                                            #type: ignore
axes[1].xaxis.set_major_locator(ticker.MultipleLocator(0.1))    #type: ignore
axes[1].axis('tight')                                           #type: ignore
axes[1].set_title('Ovisnost dometa o konstanti otpora zraka')   #type: ignore
plt.show()
