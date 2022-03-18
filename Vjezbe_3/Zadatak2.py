import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


import Zadatak1 as prt

v0 = 10
kut = 60
g = 9.81
vrijeme = np.arange(0.001, 1, 0.001)
error = []

tijelo = prt.Particle()             #type: ignore
tijelo.set_initial_conditions(v0, kut, 0, 0)

i = 0.001
while i <= 1:
    error.append((abs(((v0)**2 /g)*np.sin(2*(kut / 180)*np.pi) - tijelo.range(i)) / ((v0)**2 /g)*np.sin(2*(kut / 180)*np.pi))*100)
    tijelo.reset()
    tijelo.set_initial_conditions(v0, kut, 0, 0)
    i += 0.001

fig = plt.figure(figsize=(12,4.5), dpi=120)
axes = fig.add_axes([0.1, 0.1, 0.85, 0.75])
axes.plot(vrijeme, error, 'k', lw=0.6)
axes.set_xlabel('vrijednost dt    [s]')
axes.set_ylabel('odstupanje od analitičkog riješenja    [%]')
axes.xaxis.set_major_locator(ticker.MultipleLocator(0.05))
axes.set_title('Graf pogreške')
axes.grid(lw=0.25)
plt.show()

