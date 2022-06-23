class VertikalniHitac:
    def __init__(self):
        self.y = []
        self.v = []
        
    def set_initial_conditions(self, hight, speed):
        self.y.append(hight)
        self.v.append(speed)
        print('Objekt uspješno stvoren.\npočetna visina: {}'.format(self.y[-1]),'\npočetna brzina: {}'.format(self.v[-1]))



projectile = VertikalniHitac()
projectile.set_initial_conditions(9, 10)