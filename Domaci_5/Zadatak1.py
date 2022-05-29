import electromagnetic_field as em                  #type: ignore
import matplotlib.pyplot as plt
import numpy as np



E = np.array([0., 0., 0.])

def function_B0(t):
    Bx = 0.
    By = 0.
    Bz = em.power(4.25, -10)
    return np.array([Bx, By, Bz])

def function_B(t):
    Bx = 0.
    By = 0.
    Bz = t/10
    return np.array([Bx, By, Bz])

coordinates = np.array([0., 0., 0.])
mass = em.power(9.11, -31)
charge_e = em.power(-1, -19)
charge_p = em.power(1, -19)
dt = 0.001
time = 10
velocity = np.array([150., 150., 10.])

ele1 = em.ElectromagneticField(coordinates, mass, charge_e, E, function_B, velocity)
ele2 = em.ElectromagneticField(coordinates, mass, charge_e, E, function_B0, velocity)
poz = em.ElectromagneticField(coordinates, mass, charge_p, E, function_B, velocity)

x1, y1, z1 = ele1.moveit_RK4(dt, time)
x2, y2, z2 = ele2.moveit_RK4(dt, time)
x3, y3, z3 = poz.moveit_RK4(dt, time)


fig = plt.figure(figsize=(16, 9), dpi=70)
plt.rcParams.update({'font.size': 10})                          #type: ignore
plt.subplots_adjust(wspace=0.4, hspace=0.5)
axes = plt.axes(projection ='3d')
axes.plot3D(x1, y1, z1, 'g')
axes.plot3D(x2, y2, z2, 'y')
axes.set_xlabel('x  $[m]$')
axes.set_ylabel('y  $[m]$')
axes.set_zlabel('z  $[m]$')
axes.grid(lw=0.5)
axes.legend(['changing field', 'constant field'], loc='best')
axes.set_title('Electron in changing and constant EM field')
plt.show()


fig = plt.figure(figsize=(16, 9), dpi=70)
plt.rcParams.update({'font.size': 10})                          #type: ignore
plt.subplots_adjust(wspace=0.4, hspace=0.5)
axes = plt.axes(projection ='3d')
axes.plot3D(x1, y1, z1, 'b')
axes.plot3D(x3, y3, z3, 'r')
axes.set_xlabel('x  $[m]$')
axes.set_ylabel('y  $[m]$')
axes.set_zlabel('z  $[m]$')
axes.grid(lw=0.5)
axes.legend(['electron', 'positron'], loc='best')
axes.set_title('Electron and positron in changing EM field')
plt.show()


