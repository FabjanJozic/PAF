import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tick


class VertikalniHitac:
    def __init__(self):
        self.y = []
        self.v = []
        self.t = []
        self.dt = []
        self.a = []
        self.g = []
        self.k = []
        
    def set_initial_conditions(self, hight, speed, constant, dt):
        self.y.append(hight)
        self.a.append(0)
        self.t.append(0)
        self.dt.append(dt)
        self.v.append(speed)
        self.k.append(constant)
        self.g.append(9.81)

    def change_hight(self, hight):
        self.y.append(hight)
        
    def change_velocity(self, speed):
        self.v.append(speed)
        
    def info(self):
        print('\nvisina: {}'.format(self.y[-1]), '\nbrzina: {}'.format(self.v[-1]),'\n')
        
    def __move(self, dt):
        self.a.append(-self.g[-1]-np.sign(self.v[-1])*self.k[-1]*self.v[-1])
        self.v.append(self.v[-1]+self.a[-1]*dt)
        self.y.append(self.y[-1]+self.v[-1]*dt)
        self.t.append(self.t[-1]+dt)
        
    def reset(self):
        self.__init__()
        
    def plot_h_t(self, hight, speed, constant, dt):
        self.reset()
        self.set_initial_conditions(hight, speed, constant, dt)
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
    
    def plot_v_t(self, hight, speed, constant, dt):
        self.reset()
        self.set_initial_conditions(hight, speed, constant, dt)
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
    
    
    


h = 10
v = 10
k = 1.7
dt1 = 0.01
dt2 = 0.05
dt3 = 0.1

p1 = VertikalniHitac()
p2 = VertikalniHitac()
p3 = VertikalniHitac()

p1.set_initial_conditions(h, v, k, dt1)
p2.set_initial_conditions(h, v, k, dt2)
p3.set_initial_conditions(h, v, k, dt3)

print('Kada je dt={}, maksimalna visina je {}, a vrijeme pada je {}.\n'.format(dt1, p1.max_hight(dt1), p1.max_time(dt1)))
print('Kada je dt={}, maksimalna visina je {}, a vrijeme pada je {}.\n'.format(dt2, p2.max_hight(dt2), p2.max_time(dt2)))
print('Kada je dt={}, maksimalna visina je {}, a vrijeme pada je {}.\n'.format(dt3, p3.max_hight(dt3), p1.max_time(dt3)))
