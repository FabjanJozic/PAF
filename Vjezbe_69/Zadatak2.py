class VertikalniHitac:
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
        
    def change_velocity(self, speed):
        self.vx.append(speed)
        
    def info(self):
        print('\nvisina: {}'.format(self.y[-1]), '\nhorizontalna brzina: {}'.format(self.vx[-1]),'\n')