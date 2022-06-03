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
    def __init__(self, coordinates, mass, charge, E, B, velocity):
        self.x = []
        self.y = []
        self.z = []
        self.B_t = 0
        self.E_t = 0
        self.m = mass
        self.q = charge
        self.r = coordinates
        self.x.append(self.r[0])
        self.y.append(self.r[1])
        self.z.append(self.r[2])        
        self.v = velocity
        self.E = E
        self.t = 0
        self.B = B
        self.B_t = B(self.t) 
        self.E_f = E(self.t)
        self.a = self.__acceleration(self.E_t, self.B_t, velocity)
        self.X = [self.x[-1]]
        self.Y = [self.y[-1]]
        self.Z = [self.z[-1]]
        self.V = [self.v]

    def __acceleration(self, E, B, v):
        return (self.q/self.m)*(E+np.cross(v, B))

    def __acceleration_f(self, E, B, v):
        return (self.q/self.m)*(E+np.cross(v, B))
    

    def __move_f(self, dt):
        self.E_t = self.E(self.t)
        self.B_t = self.B(self.t)
        k1v = self.__acceleration_f(self.E_t, self.B_t, self.v)*dt
        k1r = self.v*dt 
        k2v = self.__acceleration_f(self.E_t, self.B_t, self.v+k1v/2)*dt
        k2r = (self.v+k2v/2)*dt
        k3v = self.__acceleration_f(self.E_t, self.B_t, self.v+k2v/2)*dt
        k3r = (self.v+k2v/2)*dt
        k4v = self.__acceleration_f(self.E_t, self.B_t, self.v+k3v)*dt
        k4r = (self.v+k3v)*dt
        self.v += (k1v + 2*k2v + 2*k3v + k4v)/6
        self.V.append(self.v)
        self.X.append(self.X[-1]+(k1r[0]+2*k2r[0]+2*k3r[0]+k4r[0])/6)
        self.Y.append(self.Y[-1]+(k1r[1]+2*k2r[1]+2*k3r[1]+k4r[1])/6)
        self.Z.append(self.Z[-1]+(k1r[2]+2*k2r[2]+2*k3r[2]+k4r[2])/6)   
        self.t += dt

    def moveit_f(self, dt, t): 
        while self.t <= t:
            self.__move_f(dt)
        return self.X, self.Y, self.Z  

     