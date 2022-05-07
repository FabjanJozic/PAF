import projectile as pro                                    #type: ignore
import matplotlib.pyplot as plt



mass = 0.1
velocity = 25
alpha = 45
x0 = 0
y0 = 0
dt = 0.001

a = 0.5
r = 0.28   
'''
Površine kugle i kocke su u ovim odnosima duljine stranice i radijusa otprilike jednake.
Razlike u površinama moraju biti drastične da bi se uočila veća razlika u gibanju.
'''

p1 = pro.Projectile()
p2 = pro.Projectile()

p1.set_initial_conditions(mass, velocity, alpha, x0, y0)
p2.set_initial_conditions(mass, velocity, alpha, x0, y0)

p1.object_type('ball', r)
p2.object_type('cube', a)



fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 6), dpi=90)
plt.rcParams.update({'font.size': 8})                           #type: ignore
plt.axis('equal')
plt.subplots_adjust(wspace=0.4, hspace=0.9)
axes[0].plot(p1.moveit_RK4(dt)[0], p1.moveit_RK4(dt)[1], 'g')   #type: ignore
axes[0].set_xlabel('x | $[m]$')                                 #type: ignore
axes[0].set_ylabel('y | $[m]$')                                 #type: ignore
axes[0].grid(lw=0.5)                                            #type: ignore
axes[0].axis('tight')                                           #type: ignore
axes[0].set_title('Gibanje kugle u zraku')                      #type: ignore
axes[1].plot(p2.moveit_RK4(dt)[0], p2.moveit_RK4(dt)[1], 'm')   #type: ignore
axes[1].set_xlabel('x | $[m]$')                                 #type: ignore
axes[1].set_ylabel('y | $[m]$')                                 #type: ignore
axes[1].grid(lw=0.5)                                            #type: ignore
axes[1].axis('tight')                                           #type: ignore
axes[1].set_title('Gibanje kocke u zraku')                      #type: ignore
plt.show()