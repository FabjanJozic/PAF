import harmonic_oscillator as ho                #type: ignore

tijelo = ho.HarmonicOscillator()

mass = 4.5
constant = 140
velocity = 5
position = 10
time = 3.1
dt = 0.001

tijelo.set_initial_conditions(mass, constant, velocity, position)
tijelo.plot_trajectory(time, dt)