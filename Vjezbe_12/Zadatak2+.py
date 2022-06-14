import matplotlib.pyplot as plt
import matplotlib.animation as anima
from matplotlib.animation import PillowWriter, FuncAnimation
import numpy as np
import universe


au = 1.496*(10**11)
dt = 60*60*10
year = 60*60*24*365
m = 5.9722*(10**24)         #mass of Earth
M = 1.989*(10**30)          #mass of Sun
r = 6.378*(10**6)           #radius of Earth

Sun = universe.Planet('Sun', M, 0., 0., 0., 109.178*r, 'yellow', 1000)
Mercury = universe.Planet('Mercury', 0.055*m, 0.466*au, 0., 47360., 0.38*r, 'grey', 40)
Venus = universe.Planet('Venus', 0.815*m, 0.723*au, 0., 35020., 0.949*r, 'orange', 90)
Earth = universe.Planet('Earth', m, au, 0., 29783., r, 'blue', 100)
Mars = universe.Planet('Mars', 0.107*m, 1.666*au, 0., 24077., 0.532*r, 'red', 65)

system = universe.Universe()
system.add_planet(Sun)
system.add_planet(Mercury)
system.add_planet(Venus)
system.add_planet(Earth)
system.add_planet(Mars)




system.evolve(5*year, dt)

fig = plt.figure()
metadata = dict(title="Solar system", artist="Fabjan Jozic")
writer = PillowWriter(fps=15, metadata=metadata)                        #type: ignore
with writer.saving(fig, "solar_system.gif", 100):
    for i in range(len(Mercury.x)):
        if i%5 == 0:
            plt.clf()
            for j in system.planets:               
                plt.plot(j.x[:i], j.y[:i], color =j.collor, lw=0.4)
                plt.scatter(j.x[i], j.y[i], color=j.collor, s=j.size, label=j.name)
            plt.xlim(-2.5*au, 2.5*au)
            plt.ylim(-2.5*au, 2.5*au)
            plt.axis('equal')

            writer.grab_frame()