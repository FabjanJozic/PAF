import Bullet as b


h0 = 2.
v0 = 100.
dt = 0.01

e = b.Bullet(h0, v0)
e.set_dt(dt)
e.plot_graphs()