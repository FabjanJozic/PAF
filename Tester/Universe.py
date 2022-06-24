import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter




class Planet():
    def __init__(self, name, mass, distance, velocity, radius, collor, size):
        self.velocity = velocity
        self.radius = radius
        self.mass = mass
        self.name = name
        self.r = distance
        self.x = [distance[0]]
        self.y = [distance[1]]
        self.collor = collor
        self.size = size



class Universe():
    def __init__(self):
        self.planets = []
        self.t = [0]
        self.G = 6.67408*(10**(-11))
        
    def add_planet(self, planet):
        self.planets.append(planet)
        
    def reset(self):
        self.__init__()
        
    def __move(self, dt):
        for planet1 in self.planets:
            force = np.array([0., 0.])
            for planet2 in self.planets:
                if planet2 != planet1:
                    r_x = planet1.x[-1]-planet2.x[-1]
                    r_y = planet1.y[-1]-planet2.y[-1]
                    r = np.sqrt(r_x**2+r_y**2)
                    force[0] += -self.G*planet1.mass*planet2.mass/(r**2)*(r_x/r)
                    force[1] += -self.G*planet1.mass*planet2.mass/(r**2)*(r_y/r)
                    if r <= (planet1.radius+planet2.radius):
                        break
            planet1.acceleration = np.array([force[0]/planet1.mass, force[1]/planet1.mass])
            planet1.velocity = np.array([planet1.velocity[0]+planet1.acceleration[0]*dt, planet1.velocity[1]+planet1.acceleration[1]*dt])
            planet1.x.append(planet1.x[-1]+planet1.velocity[0]*dt)
            planet1.y.append(planet1.y[-1]+planet1.velocity[1]*dt)
        self.t.append(self.t[-1]+dt)       
            
    def evolve(self, time, dt):
        while self.t[-1] <= time:
            self.__move(dt)
            
    def plot(self, time, dt, title):
        self.evolve(time, dt)
        fig = plt.figure(figsize=(12,6), dpi=110)
        plt.rcParams.update({'font.size': 8})                            #type: ignore
        axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        axes.axis('equal')
        axes.set_aspect('equal')
        axes.set_facecolor("black")
        axes.grid(lw=0.1)
        axes.set_title(title)
        for i in self.planets:
            axes.plot(i.x, i.y, color=i.collor, lw=0.1)
            axes.scatter(i.x[-1], i.y[-1], label=i.name, color=i.collor, s=i.size)
        axes.legend(loc='upper right')
        plt.show()
    
    def gif(self, time, dt, title):
        self.evolve(time, dt)
        qq = self.planets[0]
        fig = plt.figure()
        metadata = dict(title=title, author='')
        writer = PillowWriter(fps=15, metadata=metadata)                        #type: ignore
        with writer.saving(fig, "universe.gif", 100):
            for i in range(len(qq.x)):
                if i%5 == 0:
                    plt.clf()
                    for j in self.planets:               
                        plt.plot(j.x[:i], j.y[:i], color =j.collor, lw=0.1)
                        plt.scatter(j.x[i], j.y[i], color=j.collor, s=j.size, label=j.name)
                    plt.axis('equal')
                    writer.grab_frame()