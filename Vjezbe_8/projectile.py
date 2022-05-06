import numpy as np
import matplotlib.pyplot as plt





class Projectile:
    def __init__(self):
        self.vx = []
        self.vy = []
        self.t = []
        self.angle = []
        self.x = []
        self.y = []
        self.dt = []
        self.ax = []
        self.ay = []
        self.density = []
        self.Cd = []
        self.m = []
        self.A = []
        self.g = []
        
    def set_initial_conditions(self, mass, v0, alpha, x0, y0):
        self.vx.append(v0 * np.cos((alpha / 180)*np.pi))
        self.vy.append(v0 * np.sin((alpha / 180)*np.pi))
        self.t.append(0)
        self.angle.append(alpha)
        self.x.append(x0)
        self.y.append(y0)
        self.dt.append(0.001)
        self.ax.append(0)
        self.ay.append(0)
        self.g.append(-9.81)
        self.m.append(mass)
        
    def set_parameters(self, constant, area, rho):
        self.Cd.append(constant)
        self.A.append(area)
        self.density.append(rho)
    
    def reset(self):
        self.__init__()
        
    def __acceleration_x(self, x, v, t):
        return -np.sign(v)*(self.density[-1]*self.Cd[-1]*self.A[-1])/(2*self.m[-1])*(v)**2
    
    def __acceleration_y(self, x, v, t):
        return self.g[-1]-np.sign(v)*(self.density[-1]*self.Cd[-1]*self.A[-1])/(2*self.m[-1])*(v)**2
        
    def __move_RK4(self, dt):
        k_1vx = self.__acceleration_x(self.x[-1], self.vx[-1], self.t[-1])*dt
        k_1vy = self.__acceleration_y(self.y[-1], self.vy[-1], self.t[-1])*dt
        k_1x = self.vx[-1]*dt
        k_1y = self.vy[-1]*dt
        k_2vx = self.__acceleration_x(self.x[-1]+k_1x/2, self.vx[-1]+k_1vx/2, self.t[-1]+dt/2)*dt
        k_2vy = self.__acceleration_y(self.y[-1]+k_1y/2, self.vy[-1]+k_1vy/2, self.t[-1]+dt/2)*dt
        k_2x = (self.vx[-1]+k_1vx/2)*dt
        k_2y = (self.vy[-1]+k_1vy/2)*dt
        k_3vx = self.__acceleration_x(self.x[-1]+k_2x/2, self.vx[-1]+k_2vx/2, self.t[-1]+dt/2)*dt
        k_3vy = self.__acceleration_y(self.y[-1]+k_2y/2, self.vy[-1]+k_2vy/2, self.t[-1]+dt/2)*dt
        k_3x = (self.vx[-1]+k_2vx/2)*dt
        k_3y = (self.vy[-1]+k_2vy/2)*dt
        k_4vx = self.__acceleration_x(self.x[-1]+k_3x, self.vx[-1]+k_3vx, self.t[-1]+dt)*dt
        k_4vy = self.__acceleration_y(self.x[-1]+k_3y, self.vx[-1]+k_3vy, self.t[-1]+dt)*dt
        k_4x = (self.vx[-1]+k_3vx)*dt
        k_4y = (self.vy[-1]+k_3vy)*dt
        self.vx.append(self.vx[-1]+(k_1vx+2*k_2vx+2*k_3vx+k_4vx)/6)
        self.vy.append(self.vy[-1]+(k_1vy+2*k_2vy+2*k_3vy+k_4vy)/6)
        self.x.append(self.x[-1]+(k_1x+2*k_2x+2*k_3x+k_4x)/6)
        self.y.append(self.y[-1]+(k_1y+2*k_2y+2*k_3y+k_4y)/6)
        self.t.append(self.t[-1]+dt)
        return self.vx[-1], self.vx[-1], self.x[-1], self.y[-1], self.t[-1]

    def __move_Euler(self, dt):
        self.t.append(self.t[-1]+dt)
        self.ax.append(-np.sign(self.vx[-1])*(self.density[-1]*self.Cd[-1]*self.A[-1])/(2*self.m[-1])*(self.vx[-1])**2)
        self.ay.append(self.g[-1]-np.sign(self.vy[-1])*(self.density[-1]*self.Cd[-1]*self.A[-1])/(2*self.m[-1])*(self.vy[-1])**2)
        self.vx.append(self.vx[-1]+self.ax[-1]*dt)
        self.vy.append(self.vy[-1]+self.ay[-1]*dt)
        self.x.append(self.x[-1]+self.vx[-1]*dt)
        self.y.append(self.y[-1]+self.vy[-1]*dt)
        return self.ax[-1], self.ay[-1], self.vx[-1], self.vy[-1], self.x[-1], self.y[-1], self.t[-1]
    
    def range_E(self, dt):
        while self.y[-1] >= 0:
            self.__move_Euler(dt)
        return self.x[-1]
    
    def range_RK4(self, dt):
        while self.y[-1] >= 0:
            self.__move_RK4(dt)
        return self.x[-1]
    
    def moveit_E(self, dt):
        while self.y[-1] >= 0:
            self.__move_Euler(dt)
        return self.x, self.y
    
    def moveit_RK4(self, dt):
        while self.y[-1] >= 0:
            self.__move_RK4(dt)
        return self.x, self.y
    
    def plot_xy_E(self, dt):
        while self.y[-1] >= 0:
            self.__move_Euler(dt)  
        fig = plt.figure(figsize=(10,5.5), dpi=90)
        axes = fig.add_axes([0.15, 0.15, 0.75, 0.75])
        axes.plot(self.x, self.y, 'g')
        axes.set_xlabel('x | $[m]$')
        axes.set_ylabel('y | $[m]$')
        axes.grid(lw=0.5)
        axes.set_title("xy - graph\nEuler's method")
        return plt.show()

    def plot_xy_RK4(self, dt):
        while self.y[-1] >= 0:
            self.__move_RK4(dt)  
        fig = plt.figure(figsize=(10,5.5), dpi=90)
        axes = fig.add_axes([0.15, 0.15, 0.75, 0.75])
        axes.plot(self.x, self.y, 'g')
        axes.set_xlabel('x | $[m]$')
        axes.set_ylabel('y | $[m]$')
        axes.grid(lw=0.5)
        axes.set_title("xy - graph\nfourth-order Runge-Kutta method")
        return plt.show()
    
    def credibility(self, dt):
        good = False
        while self.y[-1] >= 0:
            self.__move_Euler(dt)
        if self.y[-1] < -0.01:
            good = False
        else:
            good = True
        return good
        