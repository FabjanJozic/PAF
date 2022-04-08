import numpy as np
import matplotlib.pyplot as plt


K = 200
F = 15
m = 10
dt = 0.001

'''def force(v, x, t):
    return F'''

'''def force(v, x, t):
    return -K*x'''

def force(v, x, t):
    return v/t + 3*x/(t**2)



class Force():
    def __init__(self):
        self.m = []
        self.K = []
        self.t = []
        self.x = []
        self.v = []
        self.a = []
        self.dt = []
        
    def reset(self):
        self.__init__()
        
    def set_initial_conditions(self, v0, x0, t0):
        self.m.append(m)
        self.K.append(K)
        self.t.append(t0)
        self.x.append(x0)
        self.v.append(v0)
        self.a.append(force(self.v[-1], self.x[-1], self.t[-1])/self.m[-1])
        self.dt.append(dt)
        
    def __move(self):
        self.a.append(force(self.v[-1], self.x[-1], self.t[-1])/self.m[-1])
        self.v.append(self.v[-1] + self.a[-1]*self.dt[-1])
        self.x.append(self.x[-1] + self.v[-1]*self.dt[-1])
        self.t.append(self.t[-1] + self.dt[-1])
        return self.a, self.v, self.x, self.t
    
    def plot_trajectory(self, t):
        while self.t[-1] <= t:
            self.__move()
        fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 6), dpi=80)
        plt.subplots_adjust(wspace=0.4, hspace=0.5)
        plt.rcParams.update({'font.size': 8})           #type: ignore
        plt.axis('equal')
        axes[0].plot(self.t, self.a, 'b')                                #type: ignore
        axes[0].set_xlabel('vrijeme gibanja  [$s$]')                     #type: ignore
        axes[0].set_ylabel('akceleracija  [$m/s^2$]')                    #type: ignore
        axes[0].grid(lw=0.5)                                             #type: ignore
        axes[0].axis('tight')                                            #type: ignore
        axes[1].plot(self.t, self.v, 'r')                                #type: ignore
        axes[1].set_xlabel('vrijeme gibanja  [$s$]')                     #type: ignore
        axes[1].set_ylabel('brzina  [$m/s$]')                            #type: ignore
        axes[1].grid(lw=0.5)                                             #type: ignore
        axes[1].axis('tight')                                            #type: ignore
        axes[2].plot(self.t, self.x, 'g')                                #type: ignore
        axes[2].set_xlabel('vrijeme gibanja  [$s$]')                     #type: ignore
        axes[2].set_ylabel('položaj  [$m$]')                             #type: ignore
        axes[2].grid(lw=0.5)                                             #type: ignore
        axes[2].axis('tight')                                            #type: ignore
        return plt.show()



sila = Force()
sila.set_initial_conditions(0, 1, 1)
sila.plot_trajectory(6)