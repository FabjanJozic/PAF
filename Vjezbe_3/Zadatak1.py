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
        self.dt = 0.001
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
        self.dt = 0.001
        self.ax = [0]
        self.ay.append(-9.81)
    
    def reset(self):
        '''
        Funkcija resetira i poništava vrijednosti klase.
        '''
        self.__init__()
    
    def __move(self):
        '''
        Funkcija jednom pomiče objekt u vremenskom intervalu dt.
        '''
        self.t.append(self.t[-1]+ self.dt)
        self.vx.append(self.vx[-1] + self.ax[-1]*self.dt)
        self.vy.append(self.vy[-1]+ self.ay[-1]*self.dt)
        self.x0.append(self.x0[-1]+ self.vx[-1]*self.dt)
        self.y0.append(self.y0[-1]+ self.vy[-1]*self.dt)
        return self.x0[-1], self.y0[-1]
    
    def range(self):
        '''
        Funkcija računa domet objekta ako ima putanju kosog hica.
        '''
        while self.y0[-1] >= 0:
            self.__move()
        return self.x0[-1]
    
    def plot_trajectory(self):
        '''
        Funkcija crta xy-graf gibanja objekta opisanog kao kosi hitac u vremenu koje zadaje
        korisnik.
        '''
        while self.y0[-1] >= 0:
            self.__move()  
        fig = plt.figure(figsize=(5,3), dpi=200)
        axes = fig.add_axes([0.15, 0.15, 0.75, 0.75])
        axes.plot(self.x0, self.y0, 'r')
        axes.set_xlabel('$x | [m]$')
        axes.set_ylabel('$y | [m]$')
        axes.grid()
        return plt.show()
    
p1 = Particle()
p1.set_initial_conditions(30, 20, 0, 0)
p1.plot_trajectory()
print(p1.range())