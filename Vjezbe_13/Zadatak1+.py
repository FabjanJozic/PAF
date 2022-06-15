import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter

import universe




au = 1.496*(10**11)
dt = 60*60*10
year = 60*60*24*365
m = 5.9722*(10**24)         #mass of Earth
M = 1.989*(10**30)          #mass of Sun
r = 6.378*(10**6)           #radius of Earth

Sun = universe.Planet('Sun', M, np.array([0., 0.]), np.array([0., 0.]), 109.178*r, 'yellow', 200)
Mercury = universe.Planet('Mercury', 0.055*m, np.array([0.466*au, 0.]), np.array([0., 47360.]), 0.38*r, 'grey', 8)
Venus = universe.Planet('Venus', 0.815*m, np.array([0.723*au, 0.]), np.array([0., 35020.]), 0.949*r, 'orange', 18)
Earth = universe.Planet('Earth', m, np.array([au, 0.]), np.array([0., 29783.]), r, 'blue', 20)
Mars = universe.Planet('Mars', 0.107*m, np.array([1.666*au, 0.]), np.array([0., 24077.]), 0.532*r, 'red', 13)
comet = universe.Planet('comet', 10**14, np.array([0., 4*au]), np.array([7500., -12990.]), 2000., 'black', 2)

system = universe.Universe()
system.add_planet(Sun)
system.add_planet(Mercury)
system.add_planet(Venus)
system.add_planet(Earth)
system.add_planet(Mars)
system.add_planet(comet)




system.evolve(4*year, dt)

fig = plt.figure(figsize=(14,7), dpi=100)
metadata = dict(title="Solar system with comet", artist="Fabjan Jozic")
writer = PillowWriter(fps=15, metadata=metadata)                        #type: ignore
with writer.saving(fig, "comet.gif", 100):
    for i in range(len(Mercury.x)):
        if i%5 == 0:
            plt.clf()
            for j in system.planets:               
                plt.plot(j.x[:i], j.y[:i], color =j.collor, lw=0.4)
                plt.scatter(j.x[i], j.y[i], color=j.collor, s=j.size, label=j.name)
            plt.axis('equal')
            writer.grab_frame()

