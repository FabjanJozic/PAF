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
    
    def total_time(self, dt):
        '''
        Funkcija vraća ukupno vrijeme gibanja tijela prilikom kosog hica.
        '''
        while self.y0[-1] >= 0:
            self.t.append(self.t[-1]+ dt)
            self.__move(dt)
        return self.t[-1]
    
    def max_speed(self, dt):
        '''
        Funkcija vraća najveću postignutu brzinu za tijelo dok se giba po
        putanji kosog hica.
        '''
        brzina = []
        while self.y0[-1] >= 0:
            self.vx.append(self.vx[-1]+ self.ax[0] * dt)
            self.vy.append(self.vy[-1]+ self.ay[0] * dt)
            brzina.append(math.sqrt(self.vx[-1]**2 + self.vy[-1]**2))
            self.__move(dt)
        return max(brzina)

    def velocity_to_hit_target(self,x0, y0, kut, Sx, Sy, r):
        '''
        Funkcija koja za zadani kut računa potrebnu početnu brzinu da se pogodi
        kuglica zadanog položaja i radijusa.

        '''
        brzina = []
        v = 0
        while v <= 250:
            bum = False
            self.reset()
            self.set_initial_conditions(v, kut, x0, y0)
            while self.y0[-1] >= 0:
                self.__move(0.05)
                x = self.x0[-1] - Sx
                y = self.y0[-1] - Sy
                if x**2 + y**2 <= r**2:
                    bum = True
            if bum == True:
                brzina.append(v)
            v += 0.1
        return sum(brzina)/len(brzina)
            
    
    def angle_to_hit_target(self, x0, y0, v0, Sx, Sy, r):
        '''
        Funkcija koja za zadanu početnu brzinu računa kut otklona da se pogodi
        kuglica zadanog položaja i radijusa.

        '''
        kut1 = []
        kut2 = []
        kut_1 = 0
        kut_2 = 45
        try: 
            while kut_1 >= 0 and kut_1 < 45:
                bum1 = False
                self.reset()
                self.set_initial_conditions(v0, kut_1, x0, y0)
                while self.y0[-1] >= 0:
                    self.__move(0.05)
                    a = self.x0[-1] - Sx
                    b = self.y0[-1] - Sy
                    if a**2 + b**2 <= r**2:
                        bum1 = True
                if bum1 == True:
                    kut1.append(kut_1)
                kut_1 += 0.1
            while kut_2 < 90:
                bum2 = False
                self.reset()
                self.set_initial_conditions(v0, kut_2, x0, y0)
                while self.y0[-1] >= 0:
                    self.__move(0.05)
                    c = self.x0[-1] - Sx
                    d = self.y0[-1] - Sy
                    if c**2 + d**2 <= r**2:
                        bum2 = True
                if bum2 == True:
                    kut2.append(kut_2)
                kut_2 += 0.1
            return sum(kut1)/len(kut1), sum(kut2)/len(kut2)
        except ZeroDivisionError:
            print('\n Zadana brzina je premala da se meta pogodi. Povečajte početnu brzinu. \n')




'''p = Particle()
p.set_initial_conditions(24.5, 60, 0, 0)
print(p.velocity_to_hit_target(0, 0, 45, 15, 9, 4))
print(p.angle_to_hit_target(0, 0, 12, 10, 3, 1))'''