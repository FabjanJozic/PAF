import projectile as pro                #type:ignore
import numpy as np


mass = 2.8
velocity = 21
alpha = 45
x0 = 0
y0 = 0
resistivity_constant = 0.35
surface_area = 1.78
air_density = 0.0015


p = pro.Projectile()



list_dt = np.arange(0.0001, 0.01, 0.0001)

for dt in list_dt:
    p.reset()
    p.set_initial_conditions(mass, velocity, alpha, x0, y0)
    p.set_parameters(resistivity_constant, surface_area, air_density)
    if not p.credibility(dt):
        print('Da bi rezultat bio fizikalan, interval vremena mora biti manji od {}s.'.format(dt))
        p.plot_xy_E(dt)
        break
        



