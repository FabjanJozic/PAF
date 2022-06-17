import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter

import universe as u


au = 1.496*(10**11)
dt = 60*60*10
year = 60*60*24*365
m = 5.9722*(10**24)         #mass of Earth
M = 1.989*(10**30)          #mass of Sun
r = 6.378*(10**6)           #radius of Earth
R = 6.964*(10**8)           #radius of Sun

Sun_0 = u.Planet('Sun', M, np.array([0., 0.]), np.array([0., 0.]), R, 'yellow', 200)
Mercury_0 = u.Planet('Mercury', 0.055*m, np.array([0.466*au, 0.]), np.array([0., -47360.]), 0.38*r, 'grey', 8)
Venus_0 = u.Planet('Venus', 0.815*m, np.array([0.723*au, 0.]), np.array([0., -35020.]), 0.949*r, 'orange', 18)
Earth_0 = u.Planet('Earth', m, np.array([au, 0.]), np.array([0., -29783.]), r, 'blue', 20)
Mars_0 = u.Planet('Mars', 0.107*m, np.array([1.666*au, 0.]), np.array([0., -24077.]), 0.532*r, 'red', 13)
comet_0 = u.Planet('comet', 10**14, np.array([au, -r-2005]), np.array([19500., -56790.]), 2000., 'black', 2)

system = u.Universe()
system.add_planet(Sun_0)
system.add_planet(Mercury_0)
system.add_planet(Venus_0)
system.add_planet(Earth_0)
system.add_planet(Mars_0)
system.add_planet(comet_0)

system.evolve(2*year, dt)

Sun = u.Planet('Sun', M, np.array([Sun_0.x[-1], Sun_0.y[-1]]), np.array([0., 0.]), R, 'yellow', 200)
Mercury = u.Planet('Mercury', 0.055*m, np.array([Mercury_0.x[-1], Mercury_0.y[-1]]), np.array([0., 47360.]), 0.38*r, 'grey', 8)
Venus = u.Planet('Venus', 0.815*m, np.array([Venus_0.x[-1], Venus_0.y[-1]]), np.array([0., 35020.]), 0.949*r, 'orange', 18)
Earth = u.Planet('Earth', m, np.array([Earth_0.x[-1], Earth_0.y[-1]]), np.array([0., 29783.]), r, 'blue', 20)
Mars = u.Planet('Mars', 0.107*m, np.array([Mars_0.x[-1], Mars_0.y[-1]]), np.array([0., 24077.]), 0.532*r, 'red', 13)
comet = u.Planet('comet', 10**14, np.array([comet_0.x[-1], comet_0.y[-1]]), np.array([19500., -56790.]), 2000., 'black', 2)

Sun.velocity = -Sun_0.velocity
Mercury.velocity = -Mercury_0.velocity
Venus.velocity = -Venus_0.velocity
Earth.velocity = -Earth_0.velocity
Mars.velocity = -Mars_0.velocity
comet.velocity = -comet_0.velocity

system.reset()

system.add_planet(Sun)
system.add_planet(Mercury)
system.add_planet(Venus)
system.add_planet(Earth)
system.add_planet(Mars)
system.add_planet(comet)

system.evolve(2*year, dt)

fig = plt.figure(figsize=(14,7), dpi=100)
metadata = dict(title="Solar system with comet", artist="Fabjan Jozic")
writer = PillowWriter(fps=15, metadata=metadata)                        #type: ignore
with writer.saving(fig, "comet_to_hit_Earth.gif", 100):
    for i in range(len(Mercury.x)):
        if i%5 == 0:
            plt.clf()
            for j in system.planets:               
                plt.plot(j.x[:i], j.y[:i], color =j.collor, lw=0.4)
                plt.scatter(j.x[i], j.y[i], color=j.collor, s=j.size, label=j.name)
            plt.axis('equal')
            plt.xlim(-2.5*au, 2.5*au)
            plt.ylim(-2.5*au, 2.5*au)
            writer.grab_frame()


