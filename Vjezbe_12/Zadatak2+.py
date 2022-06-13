import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
import numpy as np
import universe


au = 1.496*(10**11)
dt = 60*60*10
year = 60*60*24*365
m = 5.9722*(10**24)         #mass of Earth
M = 1.989*(10**30)          #mass of Sun
r = 6.378*(10**6)           #radius of Earth

Sun = universe.Planet('Sun', M, 0., 0., 0., 109.178*r)
Mercury = universe.Planet('Mercury', 0.055*m, 0.466*au, 0., 47360., 0.38*r)
Venus = universe.Planet('Venus', 0.815*m, 0.723*au, 0., 35020., 0.949*r)
Earth = universe.Planet('Earth', m, au, 0., 29783., r)
Mars = universe.Planet('Mars', 0.107*m, 1.666*au, 0., 24077., 0.532*r)

system = universe.Universe()
system.add_planet(Sun)
system.add_planet(Mercury)
system.add_planet(Venus)
system.add_planet(Earth)
system.add_planet(Mars)




system.evolve(5*year, dt)

fig = plt.figure()
meta = dict(title="Solar_system.gif", artist="Fabjan Jozic")
writer = PillowWriter(fps=10, metadata=meta)                    #type: ignore
with writer.saving(fig, "Solar_system.gif", 100):
    axes = fig.add_axes([0.15, 0.15, 0.75, 0.75])
    axes.axis('equal')
    axes.set_aspect('equal')
    axes.set_facecolor("black")
    axes.plot(Sun.x, Sun.y, color="yellow")
    axes.scatter(Sun.x, Sun.y, label=Sun.name, color="yellow", s=1000)
    axes.plot(Mercury.x, Mercury.y, color="grey")
    axes.scatter(Mercury.x, Mercury.y, label=Mercury.name, color="grey", s=40)
    axes.plot(Venus.x, Venus.y, color="orange")
    axes.scatter(Venus.x, Venus.y, label=Venus.name, color="orange", s=90)
    axes.plot(Earth.x, Earth.y, color="blue")
    axes.scatter(Earth.x, Earth.y, label=Earth.name, color="blue", s=100)
    axes.plot(Mars.x, Mars.y, color="red")
    axes.scatter(Mars.x, Mars.y, label=Mars.name, color="red", s=65)
    axes.legend(loc='upper right')
    axes.xlim(-2*au, 2*au)
    axes.ylim(-2*au, 2*au)
    axes.grid(lw=0.1)
    axes.title('Sunčev sustav')
    writer.grab_frame()