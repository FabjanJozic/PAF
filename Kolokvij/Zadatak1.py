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
        print('Objekt uspješno stvoren.\npočetna visina: {}'.format(self.y[-1]),'\npočetna horizontalna brzina: {}'.format(self.vx[-1]))



projectile = ProjectileDrop()
projectile.set_initial_conditions(9, 10)