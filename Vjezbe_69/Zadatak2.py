class VertikalniHitac:
    def __init__(self):
        self.y = []
        self.v = []
        
    def set_initial_conditions(self, hight, speed):
        self.y.append(hight)
        self.v.append(speed)
        
    def change_hight(self, hight):
        self.y.append(hight)
        
    def change_velocity(self, speed):
        self.v.append(speed)
        
    def info(self):
        print('\nvisina: {}'.format(self.y[-1]), '\nbrzina: {}'.format(self.v[-1]),'\n')