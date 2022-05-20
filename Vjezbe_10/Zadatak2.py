import electromagnetic_field as em              #type: ignore
import matplotlib.pyplot as plt


part = em.ElectromagneticField()

mass = em.power(9.11, -31)
charge = em.power(-1, -19)
time = 2
dt = 0.001

part.set_initial_conditions(0., 0., 0., mass, charge)
part.set_velocity(150., 150. , 3.)
part.set_E_field(0., 0., 0.)
part.set_M_field(0., 0., em.power(4.25, -10))
x1 ,y1 ,z1 = part.moveit_RK4(dt, time)

part.reset()

part.set_initial_conditions(0., 0., 0., mass, charge)
part.set_velocity(150., 150. , 3.)
part.set_E_field(0., 0., 0.)
part.set_M_field(0., 0., em.power(4.25, -10))
x2 ,y2 ,z2 = part.moveit_E(dt, time)

fig= plt.figure(figsize=(11, 6), dpi=100)
plt.rcParams.update({'font.size': 10})                  #type: ignore
axes = plt.axes(projection ='3d')
axes.plot3D(x1, y1 , z1, 'r')
axes.plot3D(x2, y2, z2, 'b')
axes.set_xlabel('x  $[m]$')
axes.set_ylabel('y  $[m]$')
axes.set_zlabel('z  $[m]$')
axes.grid(lw=0.5)
axes.legend(["Runge-Kutta 4, dt={}s".format(dt), "Euler's method, dt={}s".format(dt)], loc='best')
plt.show()