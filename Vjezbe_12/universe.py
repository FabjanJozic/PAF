import numpy as np




class Planet():
    def __init__(self, name, mass, x0, y0, velocity, radius):
        self.velocity = np.array([0., velocity])
        self.acceleration = np.array([0., 0.])
        self.radius = radius
        self.mass = mass
        self.name = name
        self.x = [x0]
        self.y = [y0]



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
            planet1.acceleration = np.array([force[0]/planet1.mass, force[1]/planet1.mass])
            planet1.velocity = np.array([planet1.velocity[0]+planet1.acceleration[0]*dt, planet1.velocity[1]+planet1.acceleration[1]*dt])
            planet1.x.append(planet1.x[-1]+planet1.velocity[0]*dt)
            planet1.y.append(planet1.y[-1]+planet1.velocity[1]*dt)
        self.t.append(self.t[-1]+dt)       
            
    def evolve(self, time, dt):
        while self.t[-1] <= time:
            self.__move(dt)