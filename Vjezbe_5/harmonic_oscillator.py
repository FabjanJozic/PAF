import numpy as np
import matplotlib.pyplot as plt



class HarmonicOscillator:
        def __init__(self):
            self.m = []
            self.K = []
            self.v = []
            self.t = []
            self.x = []
            self.dt = []
            self.a = []
            self.ax = []
            self.ay = []
            
        def set_initial_conditions(self, m, K, v0, x):
            self.m.append(m)
            self.K.append(K)
            self.v.append(v0)
            self.t.append(0)
            self.x.append(x)
            self.dt.append(0.001)
            self.a.append((-K/m)*self.x[-1])
            self.ax.append(0)
            self.ay.append(0)
            
        def reset(self):
            self.__init__()
            
        def __move(self, dt):
            self.a.append((-self.K[-1]/self.m[-1])*self.x[-1])
            self.v.append(self.v[-1] + self.a[-1]*dt)
            self.x.append(self.x[-1] + self.v[-1]*dt)
            return self.a, self.v, self.x
            
        def plot_trajectory(self, t, dt):
            while self.t[-1] <= t:
                self.__move(dt)
            fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 6), dpi=80)
            plt.subplots_adjust(wspace=0.4, hspace=0.5)
            plt.rcParams.update({'font.size': 8})           #type: ignore
            plt.axis('equal')
            axes[0].plot(self.t, self.a, 'b')                                #type: ignore
            axes[0].set_xlabel('vrijeme titranja  [$s$]')                    #type: ignore
            axes[0].set_ylabel('akceleracija  [$m/s^2$]')                    #type: ignore
            axes[0].grid(lw=0.5)                                             #type: ignore
            axes[0].axis('tight')                                            #type: ignore
            axes[1].plot(self.t, self.v, 'r')                                #type: ignore
            axes[1].set_xlabel('vrijeme titranja  [$s$]')                    #type: ignore
            axes[1].set_ylabel('brzina  [$m/s$]')                            #type: ignore
            axes[1].grid(lw=0.5)                                             #type: ignore
            axes[1].axis('tight')                                            #type: ignore
            axes[2].plot(self.t, self.x, 'g')                                #type: ignore
            axes[2].set_xlabel('vrijeme titranja  [$s$]')                    #type: ignore
            axes[2].set_ylabel('položaj  [$m$]')                             #type: ignore
            axes[2].grid(lw=0.5)                                             #type: ignore
            axes[2].axis('tight')                                            #type: ignore
            return plt.show()
        
        def period(self, dt):
            if self.x[0] < 0:
                while self.x[-1] <= 0:
                    self.__move(0.005)
                while self.x[-1] >= 0:
                    self.t.append(self.t[-1]+ dt)
                    self.__move(dt)
            elif self.x[0] > 0:
                while self.x[-1] >= 0:
                    self.__move(0.005)
                while self.x[-1] <= 0:
                    self.t.append(self.t[-1]+ dt)
                    self.__move(dt)
            T = 2*np.pi/np.sqrt(self.K[-1]/self.m[-1])
            return 2*self.t[-1], T  
            
            
            
kugla = HarmonicOscillator()
kugla.set_initial_conditions(4, 120, 0, -10)  #Morate staviti početni položaj različit od 0.
#kugla.plot_trajectory(2.7, 0.001)
print(kugla.period(0.001))



    