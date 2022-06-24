import numpy as np

import Universe as u



au = 1.496*(10**11)
dt = 10**4
year = 60*60*24*365.242
m = 5.9722*(10**24)         #mass of Earth
M = 1.989*(10**30)          #mass of Sun
r = 6.378*(10**6)           #radius of Earth

Sun = u.Planet('Sun', M, np.array([0., 0.]), np.array([0., 0.]), 109.178*r, 'yellow', 20)
Mercury = u.Planet('Mercury', 0.055*m, np.array([0.466*au, 0.]), np.array([0., 47360.]), 0.38*r, 'grey', 1)
Venus = u.Planet('Venus', 0.815*m, np.array([0.723*au, 0.]), np.array([0., 35020.]), 0.949*r, 'orange', 2)
Earth = u.Planet('Earth', m, np.array([au, 0.]), np.array([0., 29783.]), r, 'blue', 2)
Mars = u.Planet('Mars', 0.107*m, np.array([1.666*au, 0.]), np.array([0., 24077.]), 0.532*r, 'red', 1.5)
Jupiter = u.Planet('Jupiter', 317.725*m, np.array([5.203*au, 0.]), np.array([0., 13070.]), 11.194*r, 'brown', 6)
Saturn = u.Planet('Saturn', 95.151*m, np.array([9.539*au, 0.]), np.array([0., 9690.]), 9.459*r, 'olive', 5)
Uranus = u.Planet('Uranus', 14.515*m, np.array([19.18*au, 0.]), np.array([0., 6810.]), 4.007*r, 'cyan', 3.5)
Neptune = u.Planet('Neptune', 17.057*m, np.array([30.06*au, 0.]), np.array([0., 5430.]), 3.81*r, 'pink', 3.5)

s = u.Universe()
s.add_planet(Sun)
s.add_planet(Mercury)
s.add_planet(Venus)
s.add_planet(Earth)
s.add_planet(Mars)
s.add_planet(Jupiter)
s.add_planet(Saturn)
s.add_planet(Uranus)
s.add_planet(Neptune)

time = 12*year
dt = 60*60*10
title = 'Solar system'

s.plot(time, dt, title)

#s.gif(time, dt, title)