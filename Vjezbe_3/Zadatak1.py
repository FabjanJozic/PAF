import numpy as np
import matplotlib.pyplot as plt
import math
import os




class Particle:
    def __init__(self, v0, kut, x0, y0):
        self.v0 = v0
        self.kut = kut
        self.x0 = x0
        self.y0 = y0
        
    def set_initial_conditions(self, v0, kut, x0, y0):
        '''
        Funkcija postavlja nove vrijednosti klase.
        '''
        self.v0 = v0
        self.kut = kut
        self.x0 = x0
        self.y0 = y0
    
    def reset(self):
        '''
        Funkcija resetira i poništava vrijednosti klase.
        '''
        self.v0 = None 
        self.kut = None 
        self.x0 = None
        self.y0 = None 
    
    def move(self, dt):
        '''
        Funkcija pomiče objekt u vremenskom intervalu dt koji zadaje korisnik.
        Objekt ima putanju kosog hica.
        '''
        kut_rad = (self.kut / 180)*np.pi     #type: ignore
        xbrzina = [self.v0 *np.cos(kut_rad)]
        ybrzina = [self.v0 *np.sin(kut_rad)]
        xpomak = [self.x0]
        ypomak = [self.y0]
        g = 9.81
        xbrzina.append(self.v0 *np.cos(kut_rad))
        ybrzina.append(ybrzina[0]-g*(dt))
        xpomak.append(xpomak[0] + xbrzina[-1]*(dt))
        ypomak.append(ypomak[0] + ybrzina[-1]*(dt)) 
        dx = xpomak[-1]
        dy = ypomak[-1]
        return dx, dy
    
    def range(self, t):
        '''
        Funkcija računa domet objekta ako ima putanju kosog hica. Korisnik zadaje vrijeme
        tijek kojega se odvija gibanje.
        '''
        kut_rad = (self.kut / 180)*np.pi        #type: ignore
        xbrzina = [self.v0 *np.cos(kut_rad)]
        dt = 0.001
        xpomak = [self.x0]
        for i in range(int(1000*t)):
            xbrzina.append(self.v0*np.cos(kut_rad))
            xpomak.append(xpomak[i]+xbrzina[i]*(dt))   
        xpomak.sort(reverse=True)
        domet = xpomak[0]
        return domet
    
    def plot_trajectory(self, t):
        '''
        Funkcija crta xy-graf gibanja objekta opisanog kao kosi hitac u vremenu koje zadaje
        korisnik.
        '''
        kut_rad = (self.kut / 180)*np.pi        #type: ignore
        xbrzina = [self.v0 *np.cos(kut_rad)]
        ybrzina = [self.v0 *np.sin(kut_rad)]
        g = 9.81
        dt = 0.001
        xpomak = [self.x0]
        ypomak = [self.y0]
        for i in range(int(1000*t)):
            xbrzina.append(self.v0 *np.cos(kut_rad))
            ybrzina.append(ybrzina[i]-g*(dt))
            xpomak.append(xpomak[i]+xbrzina[i]*(dt))
            ypomak.append(ypomak[i]+ybrzina[i]*(dt))   
        fig = plt.figure(figsize=(5,3), dpi=200)
        axes = fig.add_axes([0.15, 0.15, 0.75, 0.75])
        axes.plot(xpomak, ypomak, 'r')
        axes.set_xlabel('$x | [m]$')
        axes.set_ylabel('$y | [m]$')
        axes.grid()
        return plt.show()
    
