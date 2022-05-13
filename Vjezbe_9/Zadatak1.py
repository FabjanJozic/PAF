import bungee_jumping as buju                 #type: ignore



mass = 75
friction_constant = 0.85
elastic_constant = 50
body_surface = 0.4
air_density = 1.3
rope_lenght = 7.5
hight = 70

time_period = 50

jumper = buju.Bungee_Jumping()
jumper.plot_energy(time_period, mass, friction_constant, elastic_constant, body_surface, air_density, rope_lenght, hight)



