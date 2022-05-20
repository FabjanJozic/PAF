import numpy as np




def power( num, exp):
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
    def __init__(self):
        self.x = []
        self.y = []
        self.z = []
        self.E = np.array([0., 0., 0.])
        self.M = np.array([0., 0., 0.])
        self.velocity = np.array([0., 0., 0.])
        self.t = []
                     
    def set_initial_conditions(self, x0, y0, z0, mass, charge):
        self.x.append(x0)
        self.y.append(y0)
        self.z.append(z0)
        self.m = mass
        self.q = charge
        self.t.append(0)
        
    def set_velocity(self, x_coordinate, y_coordinate, z_coordinate):
        self.velocity = np.array([x_coordinate, y_coordinate, z_coordinate])
        
    def set_E_field(self, x_coordinate, y_coordinate, z_coordinate):
        self.E = np.array([x_coordinate, y_coordinate, z_coordinate])
        
    def set_M_field(self, x_coordinate, y_coordinate, z_coordinate):
        self.M = np.array([x_coordinate, y_coordinate, z_coordinate])
        
    def reset(self):
        self.__init__()
        
    def __acceleration(self, x, y, z, v, t):
        return (self.q*self.E+self.q*np.cross(v, self.M))/self.m
    
    def __move_Euler(self, dt):
        self.t.append(self.t[-1]+dt)
        self.velocity += self.__acceleration(self.x[-1], self.y[-1], self.z[-1], self.velocity, self.t[-1])*dt
        self.x.append(self.x[-1]+self.velocity[0]*dt)
        self.y.append(self.y[-1]+self.velocity[1]*dt)
        self.z.append(self.z[-1]+self.velocity[2]*dt)
        
    def __move_RK4(self, dt):
        k_1v = self.__acceleration(self.x[-1], self.y[-1], self.z[-1], self.velocity, self.t[-1])*dt
        k_1r = self.velocity*dt
        k_2v = self.__acceleration(self.x[-1]+k_1r[0]/2, self.y[-1]+k_1r[1]/2, self.z[-1]+k_1r[2]/2, self.velocity+k_1v/2, self.t[-1]+dt/2)*dt
        k_2r = (self.velocity+k_1v/2)*dt
        k_3v = self.__acceleration(self.x[-1]+k_2r[0]/2, self.y[-1]+k_2r[1]/2, self.z[-1]+k_2r[2]/2, self.velocity+k_2v/2, self.t[-1]+dt/2)*dt
        k_3r = (self.velocity+k_2v/2)*dt
        k_4v = self.__acceleration(self.x[-1]+k_3r[0], self.y[-1]+k_3r[1], self.z[-1]+k_3r[2], self.velocity+k_3v, self.t[-1]+dt)*dt
        k_4r = (self.velocity+k_3v)*dt
        self.velocity += (k_1v+2*k_2v+2*k_3v+k_4v)/6
        self.x.append(self.x[-1]+(k_1r[0]+2*k_2r[0]+2*k_3r[0]+k_4r[0])/6)
        self.y.append(self.y[-1]+(k_1r[1]+2*k_2r[1]+2*k_3r[1]+k_4r[1])/6)
        self.z.append(self.z[-1]+(k_1r[2]+2*k_2r[2]+2*k_3r[2]+k_4r[2])/6)
        self.t.append(self.t[-1]+dt)
    
    def moveit_E(self, dt, t):
        while self.t[-1] <= t:
            self.__move_Euler(dt)
        return self.x, self.y, self.z
    
    def moveit_RK4(self, dt, t):
        while self.t[-1] <= t:
            self.__move_RK4(dt)
        return self.x, self.y, self.z
    

       