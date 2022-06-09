import matplotlib.pyplot as plt
import numpy as np
import universe


au = 1.496*(10**11)
dt = 10**5
year = 60*60*24*365.242
m = 5.9742*(10**24)         #mass of Earth
r = 6.378*(10**6)           #radius of Earth

Sun = universe.Planet()
Sun.set_initial_conditions('Sun', 332931.606*m, np.array([0., 0.]), np.array([0., 0.]), 109.178*r)
Mercury = universe.Planet()
Mercury.set_initial_conditions('Mercury', 0.055*m, np.array([0.466*au, 0.]), np.array([0., -47360.]), 0.38*r)
Venus = universe.Planet()
Venus.set_initial_conditions('Venus', 0.815*m, np.array([0.723*au, 0.]), np.array([0., -35020.]), 0.949*r)
Earth = universe.Planet()
Earth.set_initial_conditions('Earth', m, np.array([1.*au, 0.]), np.array([0., -29783.]), r)
Mars = universe.Planet()
Mars.set_initial_conditions('Mars', 0.107*m, np.array([1.666*au, 0.]), np.array([0., -24077.]), 0.532*r)

system = universe.Universe()
system.add_planet(Sun)
system.add_planet(Mercury)
system.add_planet(Venus)
system.add_planet(Earth)
system.add_planet(Mars)




system.evolve(0.05*year, dt)

fig = plt.figure(figsize=(14,7), dpi=90)
plt.rcParams.update({'font.size': 8})                            #type: ignore
axes = fig.add_axes([0.15, 0.15, 0.75, 0.75])
axes.axis('equal')
axes.set_aspect('equal')
axes.plot(Sun.x, Sun.y, color="yellow")
axes.plot(Earth.x, Earth.y, color="blue")
axes.plot(Mercury.x, Mercury.y, color="grey")
axes.plot(Venus.x, Venus.y, color="orange")
axes.plot(Mars.x, Mars.y, color="red")
axes.scatter(Sun.x[-1], Sun.y[-1], label=Sun.name, color="yellow")
axes.scatter(Mercury.x[-1], Mercury.y[-1], label=Mercury.name, color="grey")
axes.scatter(Venus.x[-1], Venus.y[-1], label=Venus.name, color="orange")
axes.scatter(Earth.x[-1], Earth.y[-1], label=Earth.name, color="blue")
axes.scatter(Mars.x[-1], Mars.y[-1], label=Mars.name, color="red")
axes.legend(loc='upper right')
axes.set_facecolor("black")
axes.grid(lw=0.1)
axes.set_title('Solar system')
plt.show()