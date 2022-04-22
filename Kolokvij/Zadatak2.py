import numpy as np
import matplotlib.pyplot as plt


class ProjectileDrop:
    def __init__(self):
        self.y = []
        self.vx = []
        self.vy = []
        
    def set_initial_conditions(self, hight, horizontal_speed):
        self.y.append(hight)
        self.vx.append(horizontal_speed)
        self.vy.append(0)

    def change_hight(self, hight):
        self.y.append(hight)
        
    def change_velocity(self, dv):
        self.vx.append(self.vx[-1] + dv)
        
    def info(self):
        print('\nvisina: {}'.format(self.y[-1]), '\nhorizontalna brzina: {}'.format(self.vx[-1]),'\n')
        

projectile = ProjectileDrop()
projectile.set_initial_conditions(10, 10)
projectile.info()
projectile.change_hight(15)
projectile.change_velocity(-2)
projectile.info()
            


