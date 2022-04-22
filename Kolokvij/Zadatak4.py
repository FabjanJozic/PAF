import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tick


class ProjectileDrop:
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
        
    def change_velocity(self, dv):
        self.vx.append(self.vx[-1]+dv)
        
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
        
    def plot_x_y(self, hight, starting_speed, dt):
        self.set_initial_conditions(hight, starting_speed, dt)
        while self.y[-1] >= 0:
           self.__move(dt)
        fig = plt.figure(figsize=(10,5), dpi=100)
        axes = fig.add_axes([0.2, 0.2, 0.7, 0.7])
        axes.plot(self.x, self.y, 'r')
        axes.set_xlabel('x | $[m]$')
        axes.set_ylabel('y | $[m]$')
        axes.set_title('x-y graf gibanja')
        axes.grid(lw=0.5)
        return plt.show()
    
    def plot_vy_t(self, hight, starting_speed, dt=0.005):
        self.set_initial_conditions(hight, starting_speed, dt)
        while self.y[-1] >= 0:
               self.__move(dt)
        fig = plt.figure(figsize=(10,5), dpi=100)
        axes = fig.add_axes([0.2, 0.2, 0.7, 0.7])
        axes.plot(self.t, self.vy, 'r')
        axes.set_xlabel('t | $[m]$')
        axes.set_ylabel('v_y | $[m/s]$')
        axes.set_title('vy-t graf gibanja')
        axes.grid(lw=0.5)
        return plt.show()
    
    def time_to_fall(self, dt):
        while self.y[-1] >= 0:
            self.__move(dt)
        return self.t[-1]
    
    



h = 2000
vx = 200
vremenski_korak = []
vrijeme_pada = []

pro = ProjectileDrop()

dt = np.linspace(0.001, 0.1, 100)

for i in range(len(dt)):
    vremenski_korak.append(dt[i])
    pro.set_initial_conditions(h, vx, dt[i])
    vrijeme_pada.append(pro.time_to_fall(dt[i]))
    pro.reset()
    
fig = plt.figure(figsize=(10,5), dpi=100)
axes = fig.add_axes([0.2, 0.2, 0.7, 0.7])
axes.plot(vremenski_korak, vrijeme_pada, 'k')
axes.set_xlabel('korak $[s]$')
axes.set_ylabel('vrijeme pada $[s]$')
axes.set_title('Graf ovisnosti trajanja pada projektila o koraku numeričkog računanja')
axes.xaxis.set_major_locator(tick.MultipleLocator(0.01))
axes.grid(lw=0.5)
plt.show()
    
    