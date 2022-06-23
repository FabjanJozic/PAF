import Zadatak2 as z


p1 = z.VertikalniHitac()
p2 = z.VertikalniHitac()

p1.set_initial_conditions(20, 5)
p2.set_initial_conditions(15, 6)
p1.info()
p2.info()

p1.change_hight(25)
p1.change_velocity(1)
p2.change_hight(10)
p2.change_velocity(8)
p1.info()
p2.info()