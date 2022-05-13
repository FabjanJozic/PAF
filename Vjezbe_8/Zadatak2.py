import projectile as pro                #type:ignore
import matplotlib.pyplot as plt

mass = 4.8
velocity = 21
alpha = 45
x0 = 0
y0 = 0
resistivity_constant = 0.32
surface_area = 1.08
air_density = 1.3
dt = 0.01

p1 = pro.Projectile()
p2 = pro.Projectile()

p1.set_initial_conditions(mass, velocity, alpha, x0, y0)
p1.set_parameters(resistivity_constant, surface_area, air_density)

p2.set_initial_conditions(mass, velocity, alpha, x0, y0)
p2.set_parameters(resistivity_constant, surface_area, air_density)


fig = plt.figure(figsize=(12,6.2), dpi=90)
axes = fig.add_axes([0.15, 0.15, 0.75, 0.75])
plt.rcParams.update({'font.size': 8})           #type: ignore
axes.plot(p1.moveit_E(dt)[0], p1.moveit_E(dt)[1], 'b')      
axes.plot(p2.moveit_RK4(dt)[0], p2.moveit_RK4(dt)[1], 'r')           
axes.set_xlabel('x | $[m]$')           
axes.set_ylabel('y | $[m]$')                 
axes.grid(lw=0.5)
axes.legend(['Euler, dt={}'.format(dt), 'Runge-Kutta 4, dt={}'.format(dt)], loc='best')
plt.show()