import solar_system as ss
import numpy as np
import matplotlib.pyplot as plt
import numpy as np


au = 1.496*(10**11)
dt = 10**4
year = 60*60*24*365.242
m = 5.9722*(10**24)         #mass of Earth
M = 1.989*(10**30)          #mass of Sun
r = 6.378*(10**6)           #radius of Earth

Sun = ss.Planet('Sun', M, 0., 0., 0., 109.178*r, 'yellow', 1000)
Earth = ss.Planet('Earth', m, au, 0., 29783., r, 'blue', 100)

system = ss.Universe()
system.add_planet(Sun)
system.add_planet(Earth)




system.evolve(5*year, dt)

fig = plt.figure(figsize=(12,6), dpi=110)
plt.rcParams.update({'font.size': 8})                            #type: ignore
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.axis('equal')
axes.set_aspect('equal')
axes.plot(Sun.x, Sun.y, color=Sun.collor, lw=0.4)
axes.plot(Earth.x, Earth.y, color=Earth.collor, lw=0.4)
axes.scatter(Sun.x[-1], Sun.y[-1], label=Sun.name, color=Sun.collor, s=Sun.size)
axes.scatter(Earth.x[-1], Earth.y[-1], label=Earth.name, color=Earth.collor, s=Earth.size)
axes.legend(loc='upper right')
axes.set_facecolor("black")
axes.grid(lw=0.1)
axes.set_title('Solar system')
plt.show()