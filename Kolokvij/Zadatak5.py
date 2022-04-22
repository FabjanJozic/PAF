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
        self.v_wind = []
        
    def set_initial_conditions(self, hight, horizontal_speed, dt):
        self.y.append(hight)
        self.x.append(0)
        self.vx.append(horizontal_speed)
        self.vy.append(0)
        self.ax.append(0)
        self.ay.append(-9.81)
        self.t.append(0)
        self.dt.append(dt)
        self.v_wind.append(0)

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
    
    def __move_with_wind(self, dt):
        self.t.append(self.t[-1]+dt)
        self.vx.append(self.vx[-1]+self.ax[-1]*dt)
        self.vy.append(self.vy[-1]+self.ay[-1]*dt)
        self.x.append(self.x[-1]+self.vx[-1]*dt+self.v_wind[-1]*dt)
        self.y.append(self.y[-1]+self.vy[-1]*dt)
        return self.x, self.y, self.vx, self.vy, self.ax, self.ay, self.t        
    
    def time_to_drop(self, wind_speed, target_coordinate_on_ground, width_of_target):
        time = []
        range_to_hit = np.linspace(target_coordinate_on_ground-abs(width_of_target), target_coordinate_on_ground+abs(width_of_target), 200)
        t = 0
        while t < 25:
            self.reset()
            self.set_initial_conditions(h, vx, dt)
            self.v_wind.append(wind_speed)
            self.t.append(t)
            hit = False
            while self.y[-1] >= 0:
                self.__move_with_wind(0.005)
                if self.x[-1] >= range_to_hit[0] and self.x[-1] <= range_to_hit[-1]:
                    hit = True
            if hit == True:
                time.append(t)
            t += 0.05
        self.reset()
        self.set_initial_conditions(h, vx, dt)
        self.v_wind.append(wind_speed)
        while self.y[-1] >= 0:
            self.__move_with_wind(dt)
        fig = plt.figure(figsize=(10,5), dpi=100)
        axes = fig.add_axes([0.2, 0.2, 0.7, 0.7])
        axes.plot(self.x, self.y, 'g')
        axes.set_xlabel('x | $[m]$')
        axes.set_ylabel('y | $[m]$')
        axes.set_title('Graf gibanja projektila pod utjecajem konstantnog vjetra')
        axes.grid(lw=0.5)
        return sum(time)/len(time), plt.show()
    
    
projectile = ProjectileDrop()

h = 700
vx = 220
dt = 0.005
brzina_vjetra_1 = 0
brzina_vjetra_2 = 30
udaljenost_mete = 100
radijus_mete = 15

projectile.time_to_drop(brzina_vjetra_1, udaljenost_mete, radijus_mete)
projectile.time_to_drop(brzina_vjetra_2, udaljenost_mete, radijus_mete)
print(projectile.time_to_drop(-20, 50, 15)[0])                
            
    
    