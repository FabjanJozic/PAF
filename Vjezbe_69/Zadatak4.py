import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tick


class VertikalniHitac:
    def __init__(self):
        self.y = []
        self.v = []
        self.t = []
        self.dt = []
        self.v = []
        self.a = []
        
    def set_initial_conditions(self, hight, speed, dt):
        self.y.append(hight)
        self.a.append(-9.81)
        self.t.append(0)
        self.dt.append(dt)
        self.v.append(speed)

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
        return  self.t, self.v, self.y
        
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
    
    def max_hight(self, dt):
        while self.y[-1] >= 0:
            self.__move(dt)
        return max(self.y)
    
    def max_time(self, dt):
        while self.y[-1] >= 0:
            self.__move(dt)
        return max(self.t)
    








projectile = VertikalniHitac()

h = 30
v = 170
vremenski_korak = []
vrijeme_pada = []
dt = np.linspace(0.001, 0.1, 150)

for i in range(len(dt)):
    vremenski_korak.append(dt[i])
    projectile.set_initial_conditions(h, v, dt[i])
    vrijeme_pada.append(projectile.max_time(dt[i]))
    projectile.reset()
    
fig = plt.figure(figsize=(12,6), dpi=80)
axes = fig.add_axes([0.15, 0.15, 0.75, 0.75])
axes.plot(vremenski_korak, vrijeme_pada, 'k')
axes.set_xlabel('dt  $[s]$')
axes.set_ylabel('vrijeme pada  $[s]$')
axes.set_title('Graf relativne pogreške vremena trajanja kosog hica u ovisnosti o odabranom koraku  dt')
axes.xaxis.set_major_locator(tick.MultipleLocator(0.01))
axes.grid(lw=0.5)
plt.show()