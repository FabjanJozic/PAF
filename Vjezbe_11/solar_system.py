import numpy as np
import matplotlib.pyplot as plt




class System():
    def __init__(self):
        self.x_Earth = []
        self.y_Earth = []
        self.x_Sun = []
        self.y_Sun = []
        self.t = 0
        self.dt = 3600
        
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
        
    def __move(self):
        d = np.sqrt((self.r_Sun[0]-self.r_Earth[0])**2+(self.r_Sun[1]-self.r_Earth[1]))
        self.a1 = -self.G*self.m_Earth/(d**3)*np.subtract(self.r_Sun, self.r_Earth)
        self.v_Sun = np.add(self.v_Sun, self.a1*self.dt)
        self.r_Sun = np.add(self.r_Sun, self.v_Sun*self.dt)
        #d2 = np.sqrt((self.r_Earth[0]-self.r_Sun[0])**2+(self.r_Earth[1]-self.r_Sun[1]))
        self.a2 = -self.G*self.m_Sun/(d**3)*np.subtract(self.r_Earth, self.r_Sun)
        self.v_Earth = np.add(self.v_Earth, self.a2*self.dt)
        self.r_Earth = np.add(self.r_Earth, self.v_Earth*self.dt)
        self.t += self.dt
        
    def plot_revolution(self, t):
        while self.t <= t:
            self.__move()
            self.x_Earth.append(self.r_Earth[0])
            self.y_Earth.append(self.r_Earth[1])
            self.x_Sun.append(self.r_Sun[0])
            self.y_Sun.append(self.r_Sun[1])
        fig = plt.figure(figsize=(14,7), dpi=90)
        axes = fig.add_axes([0.15, 0.15, 0.75, 0.75])
        axes.axis('equal')
        axes.set_aspect('equal')
        axes.plot(self.x_Sun, self.y_Sun, 'y', marker='o', markersize=8, markerfacecolor="yellow")
        axes.plot(self.x_Earth, self.y_Earth, 'b', marker='o', markersize=3, markerfacecolor="green")
        axes.set_xlabel('')
        axes.set_ylabel('')
        axes.set_facecolor("black")
        axes.set_title('Sun and Earth')
        return plt.show()
        
            