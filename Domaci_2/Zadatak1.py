import force as f               #type: ignore


mass = 20
velocity = 2
position = 11
time = 1        #pazite na dijeljenje sa 0

F = 15
K = 200

def force_rand(v,x,t):
    return 1.5*v/t - 2.5*x/(t**2)

def force_cons(v,x,t):
    return F

def force_elas(v,x,t):
    return -K*x

s1 = f.Force()
s2 = f.Force()
s3 = f.Force()

s1.set_initial_conditions(force_rand, mass, velocity, position, time)
s2.set_initial_conditions(force_cons, mass, velocity, position, time)
s3.set_initial_conditions(force_elas, mass, velocity, position, time)

s1.plot_trajectory(force_rand, 6)
s2.plot_trajectory(force_cons, 6)
s3.plot_trajectory(force_elas, 6)