import numpy as np
import matplotlib.pyplot as plt


class VertikalniHitac:
    def __init__(self):
        self.y = []
        self.x = []
        self.vx = []
        self.vy = []
        self.ax = []
        self.ay = []
        self.t = []
        self.dt = []
        
    def set_initial_conditions(self, hight, horizontal_speed, dt):
        self.y.append(hight)
        self.x.append(0)
        self.vx.append(horizontal_speed)
        self.vy.append(0)
        self.ax.append(0)
        self.ay.append(-9.81)
        self.t.append(0)
        self.dt.append(dt)

    def change_hight(self, hight):
        self.y.append(hight)
        
    def change_velocity(self, speed):
        self.vx.append(speed)
        
    def info(self):
        print('\nvisina: {}'.format(self.y[-1]), '\nhorizontalna brzina: {}'.format(self.vx[-1]),'\n')
        
    def __move(self, dt):
        self.t.append(self.t[-1]+dt)
        self.vx.append(self.vx[-1]+self.ax[-1]*dt)
        self.vy.append(self.vy[-1]+self.ay[-1]*dt)
        self.x.append(self.x[-1]+self.vx[-1]*dt)
        self.y.append(self.y[-1]+self.vy[-1]*dt)
        return self.x, self.y, self.vx, self.vy, self.ax, self.ay, self.t
        
    def reset(self):
        self.__init__()
        
    def plot_h_t(self, hight, starting_speed, dt):
        self.set_initial_conditions(hight, starting_speed, dt)
        while self.y[-1] >= 0:
           self.__move(dt)
        fig = plt.figure(figsize=(10,5), dpi=100)
        axes = fig.add_axes([0.2, 0.2, 0.7, 0.7])
        axes.plot(self.t, self.y, 'r')
        axes.set_xlabel('t  $[s]$')
        axes.set_ylabel('h  $[m]$')
        axes.set_title('h-t graf gibanja')
        axes.grid(lw=0.5)
        return plt.show()
    
    def plot_v_t(self, hight, starting_speed, dt):
        self.set_initial_conditions(hight, starting_speed, dt)
        while self.y[-1] >= 0:
               self.__move(dt)
        fig = plt.figure(figsize=(10,5), dpi=100)
        axes = fig.add_axes([0.2, 0.2, 0.7, 0.7])
        axes.plot(self.t, self.vy, 'r')
        axes.set_xlabel('t  $[m]$')
        axes.set_ylabel('vy  $[m/s]$')
        axes.set_title('vy-t graf gibanja')
        axes.grid(lw=0.5)
        return plt.show() 
    
    
    
    



h = 10
v = 10
dt = 0.01

projectile = VertikalniHitac()
projectile.plot_h_t(h, v, dt)
projectile.plot_v_t(h, v, dt)