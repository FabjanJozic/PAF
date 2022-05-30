import numpy as np




def power(num, exp):
    result = num
    i = 0
    if  exp > 1:
        while i < exp:
            result *= 10
            i += 1
    elif exp == 1:
        result = result
    elif exp == 0:
        result = 1
    elif exp < 0:
        while i < abs(exp):
            result /= 10
            i += 1
    return result


class ElectromagneticField():
    def __init__(self, coordinates, mass, charge, E, B, velocity, func):
        self.x = []
        self.y = []
        self.z = []
        self.m = mass
        self.q = charge
        self.r = coordinates
        self.x.append(self.r[0])
        self.y.append(self.r[1])
        self.z.append(self.r[2])
        self.v = velocity
        self.E = E
        self.t = 0
        self.func = func
        self.B = B

    def __acceleration(self, v):
        return (self.q/self.m)*(self.E+np.cross(v, self.B))

    def __acceleration_f(self, v):
        return (self.q/self.m)*(self.E+np.cross(v, self.func(self.t)))

    def __move(self, dt):
        k1v = self.__acceleration(self.v)*dt
        k1r = self.v*dt 
        k2v = self.__acceleration(self.v+k1v/2)*dt
        k2r = (self.v+k2v/2)*dt
        k3v = self.__acceleration(self.v+k2v/2)*dt
        k3r = (self.v+k2v/2)*dt
        k4v = self.__acceleration(self.v+k3v)*dt
        k4r = (self.v+k3v)*dt
        self.v += (k1v + 2*k2v + 2*k3v + k4v)/6
        self.x.append(self.x[-1]+(k1r[0]+2*k2r[0]+2*k3r[0]+k4r[0])/6)
        self.y.append(self.y[-1]+(k1r[1]+2*k2r[1]+2*k3r[1]+k4r[1])/6)
        self.z.append(self.z[-1]+(k1r[2]+2*k2r[2]+2*k3r[2]+k4r[2])/6)   
        self.t += dt     

    def __move_f(self, dt):
        k1v = self.__acceleration_f(self.v)*dt
        k1r = self.v*dt 
        k2v = self.__acceleration_f(self.v+k1v/2)*dt
        k2r = (self.v+k2v/2)*dt
        k3v = self.__acceleration_f(self.v+k2v/2)*dt
        k3r = (self.v+k2v/2)*dt
        k4v = self.__acceleration_f(self.v+k3v)*dt
        k4r = (self.v+k3v)*dt
        self.v += (k1v + 2*k2v + 2*k3v + k4v)/6
        self.x.append(self.x[-1]+(k1r[0]+2*k2r[0]+2*k3r[0]+k4r[0])/6)
        self.y.append(self.y[-1]+(k1r[1]+2*k2r[1]+2*k3r[1]+k4r[1])/6)
        self.z.append(self.z[-1]+(k1r[2]+2*k2r[2]+2*k3r[2]+k4r[2])/6)   
        self.t += dt 

    def moveit_f(self, dt, t): 
        while self.t <= t:
            self.__move_f(dt)
        return self.x, self.y, self.z

    def moveit(self, dt, t): 
        while self.t <= t:
            self.__move(dt)
        return self.x, self.y, self.z    

       