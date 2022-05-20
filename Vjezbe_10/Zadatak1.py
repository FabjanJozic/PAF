import electromagnetic_field as em              #type: ignore
import matplotlib.pyplot as plt



#   mv^2/r=qvB


part1 = em.ElectromagneticField()
part2 = em.ElectromagneticField()

mass = em.power(9.11, -31)
charge1 = em.power(-1, -19)
charge2 = em.power(1, -19)
time = 1.8
dt = 0.001

part1.set_initial_conditions(0., 0., 0., mass, charge1)
part1.set_velocity(150., 150. , 3.)
part1.set_E_field(0., 0., 0.)
part1.set_M_field(0., 0., em.power(4.25, -10))

part2.set_initial_conditions(0., 0., 0., mass, charge2)
part2.set_velocity(150., 150., 3.)
part2.set_E_field(0., 0., 0.)
part2.set_M_field(0., 0., em.power(4.25, -10))

x1 ,y1 ,z1 = part1.moveit_RK4(dt, time)
x2 ,y2 ,z2 = part2.moveit_RK4(dt, time)

fig= plt.figure(figsize=(11, 6), dpi=100)
plt.rcParams.update({'font.size': 10})                  #type: ignore
axes = plt.axes(projection ='3d')
axes.plot3D(x1, y1 , z1, 'r')
axes.plot3D(x2, y2, z2, 'b')
axes.set_xlabel('x  $[m]$')
axes.set_ylabel('y  $[m]$')
axes.set_zlabel('z  $[m]$')
axes.grid(lw=0.5)
axes.legend(['electron', 'positron'], loc='best')
plt.show()

