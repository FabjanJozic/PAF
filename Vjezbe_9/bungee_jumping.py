import numpy as np
import matplotlib.pyplot as plt



class Bungee_Jumping():
    def __init__(self):
        self.v = []
        self.t = []
        self.x = []
        self.y = []
        self.dt = []
        self.a = []
        self.density = []
        self.Cd = []
        self.mass = []
        self.area = []
        self.g = []
        self.l = []
        self.K = []
        self.h = []
        
    def reset(self):
        self.__init__()
        
    def set_initial_conditions(self, mass, resistivity_constant, elastic_constant, area, rho, rope_lenght, hight):
        self.v.append(0)
        self.t.append(0)
        self.x.append(0)
        self.y.append(hight)
        self.dt.append(0.0001)
        self.a.append(0)
        self.g.append(-9.81)
        self.Cd.append(resistivity_constant)
        self.K.append(elastic_constant)
        self.area.append(area)
        self.density.append(rho)
        self.l.append(rope_lenght)        
        self.mass.append(mass)
        self.h.append(hight)
        
    def __acceleration(self, x, v, t):
        if self.y[-1] < self.h[-1]-self.l[-1]:
            x = self.x[-1]  
        else:
            x = 0
        acceleration = self.g[-1]-np.sign(v)*(self.density[-1]*self.Cd[-1]*self.area[-1])/(2*self.mass[-1])*(v**2)+(self.K[-1]*x)/self.mass[-1]
        return acceleration
    
    def __move(self):
        k_1v = self.__acceleration(self.x[-1], self.v[-1], self.t[-1])*self.dt[-1]
        k_1y = self.v[-1]*self.dt[-1]
        k_2v = self.__acceleration(self.x[-1]+k_1y/2, self.v[-1]+k_1v/2, self.t[-1]+self.dt[-1]/2)*self.dt[-1]
        k_2y = (self.v[-1]+k_1v/2)*self.dt[-1]
        k_3v = self.__acceleration(self.y[-1]+k_2y/2, self.v[-1]+k_2v/2, self.t[-1]+self.dt[-1]/2)*self.dt[-1]
        k_3y = (self.v[-1]+k_2v/2)*self.dt[-1]
        k_4v = self.__acceleration(self.x[-1]+k_3y, self.v[-1]+k_3v, self.t[-1]+self.dt[-1])*self.dt[-1]
        k_4y = (self.v[-1]+k_3v)*self.dt[-1]
        self.v.append(self.v[-1]+(k_1v+2*k_2v+2*k_3v+k_4v)/6)
        self.y.append(self.y[-1]+(k_1y+2*k_2y+2*k_3y+k_4y)/6)
        self.t.append(self.t[-1]+self.dt[-1])
        self.x.append(self.h[-1]-self.l[-1]-self.y[-1])
        
    def plot_energy(self, t, mass, resistivity_constant, elastic_constant, area, rho, rope_lenght, hight):
        self.set_initial_conditions(mass, resistivity_constant, elastic_constant, area, rho, rope_lenght, hight)
        Ep_g1 = [self.mass[-1]*(-1*self.g[-1])*self.y[-1]]
        Ep_e1 = [0]
        Ek1 = [0.5*self.mass[-1]*(self.v[-1]**2)]
        E1 = [Ep_g1[-1]+Ep_e1[-1]+Ek1[-1]]
        while self.t[-1] < t:
            self.__move()
            if self.y[-1] < self.h[-1]-self.l[-1]:
                x1 = self.x[-1]  
            else:
                x1 = 0
            Ep_g1.append(self.mass[-1]*(-1*self.g[-1])*self.y[-1])
            Ep_e1.append(0.5*self.K[-1]*(x1**2))
            Ek1.append(0.5*self.mass[-1]*(self.v[-1]**2))
            E1.append(Ep_g1[-1]+Ep_e1[-1]+Ek1[-1])
        self.reset()
        self.set_initial_conditions(mass, 0, elastic_constant, area, rho, rope_lenght, hight)
        Ep_g2 = [self.mass[-1]*(-1*self.g[-1])*self.y[-1]]
        Ep_e2 = [0]
        Ek2 = [0.5*self.mass[-1]*(self.v[-1]**2)]
        E2 = [Ep_g1[-1]+Ep_e1[-1]+Ek1[-1]]        
        while self.t[-1] < t:
            if self.y[-1] < self.h[-1]-self.l[-1]:
                x2 = self.x[-1]  
            else:
                x2 = 0
            self.__move()
            Ep_g2.append(self.mass[-1]*(-1*self.g[-1])*self.y[-1])
            Ep_e2.append(0.5*self.K[-1]*(x2**2))
            Ek2.append(0.5*self.mass[-1]*(self.v[-1]**2))
            E2.append(Ep_g2[-1]+Ep_e2[-1]+Ek2[-1])
        fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(18, 10), dpi=60)
        plt.subplots_adjust(wspace=0.4, hspace=0.5)
        plt.rcParams.update({'font.size': 10})                                                                                                  #type: ignore
        plt.axis('equal')
        axes[0].plot(self.t, Ep_g1, 'r')                                                                                                        #type: ignore
        axes[0].plot(self.t, Ep_e1, 'g')                                                                                                        #type: ignore
        axes[0].plot(self.t, Ek1, 'b')                                                                                                          #type: ignore
        axes[0].plot(self.t, E1, 'k')                                                                                                           #type: ignore
        axes[0].set_xlabel('time | $[s]$')                                                                                                      #type: ignore
        axes[0].set_ylabel('energy | $[J]$')                                                                                                    #type: ignore
        axes[0].grid(lw=0.5)                                                                                                                    #type: ignore
        axes[0].axis('tight')                                                                                                                   #type: ignore
        axes[0].legend(['gravitational potential energy', 'elastic potential energy', 'kinetic energy', 'total energy'], loc='best')            #type: ignore
        axes[0].set_title('Bungee-jumping energy diagram with air resistance')                                                                  #type: ignore
        axes[1].plot(self.t, Ep_g2, 'r')                                                                                                        #type: ignore
        axes[1].plot(self.t, Ep_e2, 'g')                                                                                                        #type: ignore
        axes[1].plot(self.t, Ek2, 'b')                                                                                                          #type: ignore
        axes[1].plot(self.t, E2, 'k')                                                                                                           #type: ignore
        axes[1].set_xlabel('time | $[s]$')                                                                                                      #type: ignore
        axes[1].set_ylabel('energy | $[J]$')                                                                                                    #type: ignore
        axes[1].grid(lw=0.5)                                                                                                                    #type: ignore
        axes[1].axis('tight')                                                                                                                   #type: ignore
        axes[1].legend(['gravitational potential energy', 'elastic potential energy', 'kinetic energy', 'total energy'], loc='best')            #type: ignore              
        axes[1].set_title('Bungee-jumping energy diagram without air resistance')                                                               #type: ignore
        return plt.show()
        

    
    