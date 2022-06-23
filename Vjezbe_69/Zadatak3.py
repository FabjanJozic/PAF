import numpy as np
import matplotlib.pyplot as plt


class VertikalniHitac:
    def __init__(self):
        self.y = []
        self.a = []
        self.t = []
        self.dt = []
        self.v = []
        
    def set_initial_conditions(self, hight, speed, dt):
        self.y.append(hight)
        self.v.append(speed)
        self.a.append(-9.81)
        self.t.append(0)
        self.dt.append(dt)

    def change_hight(self, hight):
        self.y.append(hight)
        
    def change_velocity(self, speed):
        self.v.append(speed)
        
    def info(self):
        print('\nvisina: {}'.format(self.y[-1]), '\nbrzina: {}'.format(self.v[-1]),'\n')
        
    def __move(self, dt):
        self.t.append(self.t[-1]+dt)
        self.v.append(self.v[-1]+self.a[-1]*dt)
        self.y.append(self.y[-1]+self.v[-1]*dt)
        return self.y, self.t, self.v
        
    def reset(self):
        self.__init__()
        
    def plot_h_t(self, hight, starting_speed, dt):
        self.reset()
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
        self.reset()
        self.set_initial_conditions(hight, starting_speed, dt)
        while self.y[-1] >= 0:
               self.__move(dt)
        fig = plt.figure(figsize=(10,5), dpi=100)
        axes = fig.add_axes([0.2, 0.2, 0.7, 0.7])
        axes.plot(self.t, self.v, 'r')
        axes.set_xlabel('t  $[m]$')
        axes.set_ylabel('v  $[m/s]$')
        axes.set_title('v-t graf gibanja')
        axes.grid(lw=0.5)
        return plt.show()
    
    
    
    
    



h = 10
v = 10
dt = 0.01

projectile = VertikalniHitac()
projectile.plot_h_t(h, v, dt)
projectile.plot_v_t(h, v, dt)