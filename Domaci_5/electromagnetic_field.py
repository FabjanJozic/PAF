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
            result *= 0.1
            i += 1
    return result


class ElectromagneticField():
    def __init__(self, x0, y0, z0, mass, charge, E, B, v):
        self.x = []
        self.y = []
        self.z = []
        self.v = v
        self.t = 0
        self.m = mass
        self.q = charge
        self.func_E = E
        self.func_B = B
        self.E = E(self.t)
        self.B = B(self.t)
        self.a = self.__acceleration(self.v, self.B)
        self.r = np.array([x0, y0, z0])
       
    def __acceleration(self, v, B):
        return (self.q/self.m)*np.add(self.E, np.cross(v, B))
    
    def __move_Euler(self, dt):
        self.B = self.func_B(self.t)
        self.v = np.add(self.v,self.a*dt)
        self.r = np.add(self.r,self.v*dt)
        self.a = self.__acceleration(self.v, self.B)
        self.t += dt
        self.x.append(self.r[0])
        self.y.append(self.r[1])
        self.z.append(self.r[2])
                
    def __move_RK4(self, dt):
        self.B = self.func_B(self.t)
        k1v = self.__acceleration(self.v, self.B)*dt 
        k1r = self.v*dt
        k2v = self.__acceleration(np.add(self.v,k1v/2),self.B)*dt
        k2r = (np.add(self.v,k1v/2))*dt
        k3v = self.__acceleration(np.add(self.v,k2v/2),self.B)*dt
        k3r = (np.add(self.v,k2v/2))*dt
        k4v = self.__acceleration(np.add(self.v,k3v),self.B)*dt
        k4r = (np.add(self.v,k3v))*dt
        self.v += (1/6)*(k1v+2*k2v+2*k3v+k4v)
        self.r += (1/6)*(k1r+2*k2r+2*k3r+k4r)
        self.a = self.__acceleration(self.v,self.B)
        self.x.append(self.r[0])
        self.y.append(self.r[1])
        self.z.append(self.r[2])
        self.t += dt
    
    def moveit_E(self, dt, t):
        while self.t <= t:
            self.__move_Euler(dt)
        return self.x, self.y, self.z
    
    def moveit_RK4(self, dt, t):
        while self.t <= t:
            self.__move_RK4(dt)
        return self.x, self.y, self.z
    

       