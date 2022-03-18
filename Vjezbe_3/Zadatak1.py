import numpy as np
import matplotlib.pyplot as plt
import math
import os




class Particle:
    def __init__(self):
        self.vx = []
        self.vy = []
        self.t = []
        self.kut = []
        self.x0 = []
        self.y0 = []
        self.dt = []
        self.ax = []
        self.ay = []
        
    def set_initial_conditions(self, v0, kut, x0, y0):
        '''
        Funkcija postavlja nove vrijednosti klase.
        '''
        self.vx.append(v0 * np.cos((kut / 180)*np.pi))
        self.vy.append(v0 * np.sin((kut / 180)*np.pi))
        self.t.append(0)
        self.kut.append(kut)
        self.x0.append(x0)
        self.y0.append(y0)
        self.dt.append(0.001)
        self.ax.append(0)
        self.ay.append(-9.81)
    
    def reset(self):
        '''
        Funkcija resetira i poništava vrijednosti klase.
        '''
        self.__init__()
    
    def __move(self, dt):
        '''
        Funkcija jednom pomiče objekt u vremenskom intervalu dt.
        '''
        self.t.append(self.t[-1]+ dt)
        self.vx.append(self.vx[-1] + self.ax[-1]*dt)
        self.vy.append(self.vy[-1]+ self.ay[-1]*dt)
        self.x0.append(self.x0[-1]+ self.vx[-1]*dt)
        self.y0.append(self.y0[-1]+ self.vy[-1]*dt)
        return self.x0[-1], self.y0[-1]
    
    def range(self, dt):
        '''
        Funkcija računa domet objekta koji ima putanju kosog hica.
        '''
        while self.y0[-1] >= 0:
            self.__move(dt)
        return self.x0[-1]
    
    def plot_trajectory(self):
        '''
        Funkcija crta xy-graf gibanja objekta opisanog kao kosi hitac.
        '''
        while self.y0[-1] >= 0:
            self.__move(0.001)  
        fig = plt.figure(figsize=(5,3), dpi=200)
        axes = fig.add_axes([0.15, 0.15, 0.75, 0.75])
        axes.plot(self.x0, self.y0, 'g')
        axes.set_xlabel('$x | [m]$')
        axes.set_ylabel('$y | [m]$')
        axes.grid()
        return plt.show()
    
