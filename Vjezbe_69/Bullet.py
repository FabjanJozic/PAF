


class Bullet:
    def __init__(self, hight, speed):
        self.x = [0]
        self.y = [hight]
        self.vx = [speed]
        self.vy = [0]
        self.t = [0]
        self.g = -9.81
        self.dt = 0.01
        self.__print_info()
        
    def __print_info(self):
        print('pocetna visina: {}\npocetna brzina: {}\n'.format(self.y[-1], self.vx[-1]))
        
    def change_speed(self, change):
        self.vx.append(self.vx[-1]+change)
        
    def change_hight(self, change):
        self.y.append(self.y[-1]+change)
        
    def info(self):
        print('trenutna visina: {}\ntrenutna brzina: {}\n'.format(self.y[-1], self.vx[-1]))
        
    