import matplotlib.pyplot as plt
import numpy as np
import universe


au = 1.496*(10**11)
dt = 10**4
year = 60*60*24*365.242
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

fig = plt.figure(figsize=(14,7), dpi=90)
plt.rcParams.update({'font.size': 8})                            #type: ignore
axes = fig.add_axes([0.15, 0.15, 0.75, 0.75])
axes.axis('equal')
axes.set_aspect('equal')
axes.plot(Sun.x, Sun.y, color="yellow", lw=0.4)
axes.plot(Earth.x, Earth.y, color="blue", lw=0.4)
axes.plot(Mercury.x, Mercury.y, color="grey", lw=0.4)
axes.plot(Venus.x, Venus.y, color="orange", lw=0.4)
axes.plot(Mars.x, Mars.y, color="red", lw=0.4)
axes.scatter(Sun.x[-1], Sun.y[-1], label=Sun.name, color="yellow", s=1000)
axes.scatter(Mercury.x[-1], Mercury.y[-1], label=Mercury.name, color="grey", s=40)
axes.scatter(Venus.x[-1], Venus.y[-1], label=Venus.name, color="orange", s=90)
axes.scatter(Earth.x[-1], Earth.y[-1], label=Earth.name, color="blue", s=100)
axes.scatter(Mars.x[-1], Mars.y[-1], label=Mars.name, color="red", s=65)
axes.legend(loc='upper right')
axes.set_facecolor("black")
axes.grid(lw=0.1)
axes.set_title('Solar system')
plt.show()