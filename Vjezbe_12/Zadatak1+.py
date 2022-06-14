import matplotlib.pyplot as plt
import numpy as np
import universe


au = 1.496*(10**11)
dt = 10**4
year = 60*60*24*365.242
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

fig = plt.figure(figsize=(12,6), dpi=110)
plt.rcParams.update({'font.size': 8})                            #type: ignore
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.axis('equal')
axes.set_aspect('equal')
axes.plot(Sun.x, Sun.y, color=Sun.collor, lw=0.4)
axes.plot(Earth.x, Earth.y, color=Earth.collor, lw=0.4)
axes.plot(Mercury.x, Mercury.y, color=Mercury.collor, lw=0.4)
axes.plot(Venus.x, Venus.y, color=Venus.collor, lw=0.4)
axes.plot(Mars.x, Mars.y, color=Mars.collor, lw=0.4)
axes.scatter(Sun.x[-1], Sun.y[-1], label=Sun.name, color=Sun.collor, s=Sun.size)
axes.scatter(Mercury.x[-1], Mercury.y[-1], label=Mercury.name, color=Mercury.collor, s=Mercury.size)
axes.scatter(Venus.x[-1], Venus.y[-1], label=Venus.name, color=Venus.collor, s=Venus.size)
axes.scatter(Earth.x[-1], Earth.y[-1], label=Earth.name, color=Earth.collor, s=Earth.size)
axes.scatter(Mars.x[-1], Mars.y[-1], label=Mars.name, color=Mars.collor, s=Mars.size)
axes.legend(loc='upper right')
axes.set_facecolor("black")
axes.grid(lw=0.1)
axes.set_title('Solar system')
plt.show()