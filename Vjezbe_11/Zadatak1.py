import solar_system as ss
import numpy as np


o = ss.System()

m_Earth = 5.9742*(10**24)
m_Sun = 1.989*(10**30)
r_Earth = np.array((1.496*(10**11), 0.))
r_Sun = np.array((0., 0.))
v_Earth = np.array((0., 29783.))
v_Sun = np.array((0., 0.))
time = 60*60*24*365.242

o.set_initial_conditions(m_Earth, r_Earth, v_Earth, m_Sun, r_Sun, v_Sun)
o.plot_revolution(time)