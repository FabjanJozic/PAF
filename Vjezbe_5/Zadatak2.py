import harmonic_oscillator as ho            #type: ignore

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np



tijelo = ho.HarmonicOscillator()

mass = 5
constant = 150
velocity = 1
position = 15


period_n = []
period_a = []
korak = []
for e in np.arange(0.0005, 0.15, 0.0005):
    tijelo.set_initial_conditions(mass, constant, velocity, position)
    korak.append(e)
    period_n.append(tijelo.period(e)[0])
    period_a.append(tijelo.period(e)[1])
    tijelo.reset()



fig = plt.figure(figsize=(15,6.2), dpi=90)
axes = fig.add_axes([0.15, 0.15, 0.75, 0.75])
plt.rcParams.update({'font.size': 8})           #type: ignore
axes.plot(korak, period_n, 'b',marker='o', markersize=3, markerfacecolor="red")            
axes.plot(korak, period_a, 'k')      
axes.set_xlabel('korak za numeričko računanje')           
axes.set_ylabel('vrijednost perioda u sekundama')                 
axes.grid(lw=0.5)                    
axes.legend(['vrijednost perioda izračunatog numerički', 'vrijednost perioda izračunatog analitički'], loc='best')              
axes.set_title('Period harmonijskog oscilatora')
axes.xaxis.set_major_locator(ticker.MultipleLocator(0.01))
plt.show()

