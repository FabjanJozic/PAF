import Bullet as b 


metak = b.Bullet(10, 10)
l = 50.
h = 1.5
dt1 = 0.01
dt2 = 0.05
dt3 = 0.1
y0 = 2.
r = 0.1

metak.set_dt(dt1)
metak.speed_to_hit_target(l, h, y0, r)

