import projectile as pro                                                                                        #type: ignore
import matplotlib.pyplot as plt


m = 2.3
v1 = 20
v2 = 25
v3 = 30
x0 = 0
y0 = 0
dt = 0.005
A = 1.2
Cd = 0.45
rho = 0.0015

x = 8
y = 8
r = 2


p1_1 = pro.Projectile()
p1_2 = pro.Projectile()
p2_1 = pro.Projectile()
p2_2 = pro.Projectile()
p3_1 = pro.Projectile()
p3_2 = pro.Projectile()

angle1_1 = p1_1.angle_to_hit_target(m, v1, Cd, A, rho, x0, y0, r, x, y)[0]
angle1_2 = p1_2.angle_to_hit_target(m, v1, Cd, A, rho, x0, y0, r, x, y)[1]
angle2_1 = p2_1.angle_to_hit_target(m, v2, Cd, A, rho, x0, y0, r, x, y)[0]
angle2_2 = p2_2.angle_to_hit_target(m, v2, Cd, A, rho, x0, y0, r, x, y)[1]
angle3_1 = p3_1.angle_to_hit_target(m, v3, Cd, A, rho, x0, y0, r, x, y)[0]
angle3_2 = p3_2.angle_to_hit_target(m, v3, Cd, A, rho, x0, y0, r, x, y)[1]

p1_1.set_initial_conditions(m, v1, angle1_1, x0, y0)
p1_2.set_initial_conditions(m, v2, angle1_2, x0, y0)
p2_1.set_initial_conditions(m, v3, angle2_1, x0, y0)
p2_2.set_initial_conditions(m, v1, angle2_2, x0, y0)
p3_1.set_initial_conditions(m, v2, angle3_1, x0, y0)
p3_2.set_initial_conditions(m, v3, angle3_2, x0, y0)

p1_1.set_parameters(Cd, A, rho)
p1_2.set_parameters(Cd, A, rho)
p2_1.set_parameters(Cd, A, rho)
p1_2.set_parameters(Cd, A, rho)
p3_1.set_parameters(Cd, A, rho)
p3_2.set_parameters(Cd, A, rho)


fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 6), dpi=80)
plt.subplots_adjust(wspace=0.4, hspace=0.5)
plt.rcParams.update({'font.size': 8})                                                                           #type: ignore
plt.axis('equal')
circle1 = plt.Circle((x, y), r, color = 'y')
circle2 = plt.Circle((x, y), r, color = 'y')
circle3 = plt.Circle((x, y), r, color = 'y')
axes[0].plot(p1_1.moveit_RK4(dt)[0], p1_1.moveit_RK4(dt)[1], 'b--')                                             #type: ignore
axes[0].plot(p1_2.moveit_RK4(dt)[0], p1_2.moveit_RK4(dt)[1], 'r--')                                             #type: ignore
axes[0].add_patch(circle1)                                                                                      #type: ignore
axes[0].plot(0, 0, 'w')                                                                                         #type: ignore
axes[0].set_xlabel('x | $[m]$')                                                                                 #type: ignore
axes[0].set_ylabel('y | $[m]$')                                                                                 #type: ignore
axes[0].grid(lw=0.5)                                                                                            #type: ignore
axes[0].axis('equal')                                                                                           #type: ignore
axes[0].set_aspect('equal')                                                                                     #type: ignore
axes[0].legend(['angle = {}°'.format(angle1_1),                                                                 #type: ignore
                'angle = {}°'.format(angle1_2),
                'target, x = {}$m$, y = {}$m$, r = {}$m$'.format(x, y, r),
                'velocity = {}$m/s$'.format(v1)], loc='lower center')
axes[1].plot(p2_1.moveit_RK4(dt)[0], p2_1.moveit_RK4(dt)[1], 'b--')                                             #type: ignore
axes[1].plot(p2_2.moveit_RK4(dt)[0], p2_2.moveit_RK4(dt)[1], 'r--')                                             #type: ignore
axes[1].add_patch(circle2)                                                                                      #type: ignore
axes[1].plot(0, 0, 'w')                                                                                         #type: ignore
axes[1].set_xlabel('x | $[m]$')                                                                                 #type: ignore
axes[1].set_ylabel('y | $[m]$')                                                                                 #type: ignore
axes[1].grid(lw=0.5)                                                                                            #type: ignore
axes[1].axis('equal')                                                                                           #type: ignore
axes[1].set_aspect('equal')                                                                                     #type: ignore
axes[1].legend(['angle = {}°'.format(angle2_1),                                                                 #type: ignore
                'angle = {}°'.format(angle2_2),
                'target, x = {}$m$, y = {}$m$, r = {}$m$'.format(x, y, r),
                'velocity = {}$m/s$'.format(v2)], loc='lower center')
axes[2].plot(p3_1.moveit_RK4(dt)[0], p3_1.moveit_RK4(dt)[1], 'b--')                                             #type: ignore
axes[2].plot(p3_2.moveit_RK4(dt)[0], p3_2.moveit_RK4(dt)[1], 'r--')                                             #type: ignore
axes[2].add_patch(circle3)                                                                                      #type: ignore
axes[2].plot(0, 0, 'w')                                                                                         #type: ignore
axes[2].set_xlabel('x | $[m]$')                                                                                 #type: ignore
axes[2].set_ylabel('y | $[m]$')                                                                                 #type: ignore
axes[2].grid(lw=0.5)                                                                                            #type: ignore
axes[2].axis('equal')                                                                                           #type: ignore
axes[2].set_aspect('equal')                                                                                     #type: ignore
axes[2].legend(['angle = {}°'.format(angle3_1),                                                                 #type: ignore
                'angle = {}°'.format(angle3_2),
                'target, x = {}$m$, y = {}$m$, r = {}$m$'.format(x, y, r),
                'velocity = {}$m/s$'.format(v3)], loc='lower center')
plt.show()

