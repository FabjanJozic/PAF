import numpy as np
import matplotlib.pyplot as plt




class System():
    def __init__(self):
        self.x_Earth = []
        self.y_Earth = []
        self.x_Sun = []
        self.y_Sun = []
        self.t = 0
        self.dt = 500
        
    def set_initial_conditions(self, mass_Earth, position_Earth, velocity_Earth, mass_Sun, position_Sun, velocity_Sun):
        self.G = 6.67408*(10**(-11))
        self.m_Earth = mass_Earth
        self.m_Sun = mass_Sun
        self.x_Earth.append(position_Earth[0])
        self.y_Earth.append(position_Earth[1])
        self.x_Sun.append(position_Sun[0])
        self.y_Sun.append(position_Sun[1])
        self.v_Earth = velocity_Earth
        self.v_Sun = velocity_Sun
        self.r_Earth = position_Earth
        self.r_Sun = position_Sun
        
    def reset(self):
        self.__init__()
        
    def __acceleration(self, m, r1, r2):
        return -self.G*m/((np.sqrt((r1[0]-r2[0])**2+(r1[1]-r2[1])**2))**3)*np.subtract(r1, r2)
        
    def __move(self):
        r_Earth = self.r_Earth
        r_Sun = self.r_Sun
        k1v_1 = self.__acceleration(self.m_Earth, self.r_Sun, self.r_Earth)*self.dt
        k1r_1 = self.v_Sun*self.dt
        k2v_1 = self.__acceleration(self.m_Earth, self.r_Sun+k1r_1/2, self.r_Earth+k1r_1/2)*self.dt
        k2r_1 = (self.v_Sun+k1v_1/2)*self.dt
        k3v_1 = self.__acceleration(self.m_Earth, self.r_Sun+k2r_1/2, self.r_Earth+k2r_1/2)*self.dt
        k3r_1 = (self.v_Sun+k2v_1/2)
        k4v_1 = self.__acceleration(self.m_Earth, self.r_Sun, self.r_Earth)*self.dt
        k4r_1 = self.v_Sun*self.dt
        self.v_Sun = np.add(self.v_Sun, (k1v_1+2*k2v_1+2*k3v_1+k4v_1)/6)
        self.r_Sun = np.add(r_Sun, (k1r_1+2*k2r_1+2*k3r_1+k4r_1)/6)
        self.x_Sun.append(self.x_Sun[-1]+(k1r_1[0]+2*k2r_1[0]+2*k3r_1[0]+k4r_1[0])/6)
        self.y_Sun.append(self.y_Sun[-1]+(k1r_1[1]+2*k2r_1[1]+2*k3r_1[1]+k4r_1[1])/6)
        k1v_2 = self.__acceleration(self.m_Sun, self.r_Earth, self.r_Sun)*self.dt
        k1r_2 = self.v_Earth*self.dt
        k2v_2 = self.__acceleration(self.m_Sun, self.r_Earth+k1r_2/2, self.r_Sun+k1r_2/2)*self.dt
        k2r_2 = (self.v_Earth+k1v_2/2)*self.dt
        k3v_2 = self.__acceleration(self.m_Sun, self.r_Earth+k2r_2/2, self.r_Sun+k2r_2/2)*self.dt
        k3r_2 = (self.v_Earth+k2v_2/2)
        k4v_2 = self.__acceleration(self.m_Sun, self.r_Earth, self.r_Sun)*self.dt
        k4r_2 = self.v_Earth*self.dt
        self.v_Earth = np.add(self.v_Earth, (k1v_2+2*k2v_2+2*k3v_2+k4v_2)/6)
        self.r_Earth = np.add(r_Earth, (k1r_2+2*k2r_2+2*k3r_2+k4r_2)/6)
        self.x_Earth.append(self.x_Earth[-1]+(k1r_2[0]+2*k2r_2[0]+2*k3r_2[0]+k4r_2[0])/6)
        self.y_Earth.append(self.y_Earth[-1]+(k1r_2[1]+2*k2r_2[1]+2*k3r_2[1]+k4r_2[1])/6)       
        self.t += self.dt
        
    def plot_revolution(self, t):
        while self.t <= t:
            self.__move()
        fig = plt.figure(figsize=(14,7), dpi=90)
        axes = fig.add_axes([0.15, 0.15, 0.75, 0.75])
        axes.axis('equal')
        axes.set_aspect('equal')
        axes.plot(self.x_Sun, self.y_Sun, 'y', marker='o', markersize=10, markerfacecolor="orange")
        axes.plot(self.x_Earth, self.y_Earth, 'b', marker='o', markersize=3, markerfacecolor="green")
        axes.set_xlabel('')
        axes.set_ylabel('')
        axes.set_facecolor("black")
        axes.set_title('Sun and Earth')
        axes.legend(['Sun', 'Earth'], loc='best')
        return plt.show()
    
    
    







class Planet():
    def __init__(self, name, mass, x0, y0, velocity, radius, collor, size):
        self.velocity = np.array([0., velocity])
        self.acceleration = np.array([0., 0.])
        self.radius = radius
        self.mass = mass
        self.name = name
        self.x = [x0]
        self.y = [y0]
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
            planet1.acceleration = np.array([force[0]/planet1.mass, force[1]/planet1.mass])
            planet1.velocity = np.array([planet1.velocity[0]+planet1.acceleration[0]*dt, planet1.velocity[1]+planet1.acceleration[1]*dt])
            planet1.x.append(planet1.x[-1]+planet1.velocity[0]*dt)
            planet1.y.append(planet1.y[-1]+planet1.velocity[1]*dt)
        self.t.append(self.t[-1]+dt)       
            
    def evolve(self, time, dt):
        while self.t[-1] <= time:
            self.__move(dt)
        
            