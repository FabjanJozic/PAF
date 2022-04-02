import particle as pa                   #type: ignore

import matplotlib.pyplot as plt
import matplotlib.ticker as tick


v = 20      #ovo sami mijenjate
dt = 0.001
kut1 = []
kut2 = []
domet1 = []
domet2 = []
vrijeme1 = []
vrijeme2 = []

part = pa.Particle()

for a in range(0, 91):
    part.set_initial_conditions(v, a, 0, 0)
    kut1.append(a)
    domet1.append(part.range(dt))
    vrijeme1.append(part.total_time(dt))
    part.reset()
    
for b in range(0, 91):
    part.set_initial_conditions(15, b, 0, 0)
    kut2.append(b)
    domet2.append(part.range(dt))
    vrijeme2.append(part.total_time(dt))
    part.reset()

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(13.4, 5), dpi=100)
plt.subplots_adjust(wspace=0.3, hspace=0.6)
plt.rcParams.update({'font.size': 8})                            #type: ignore
plt.axis('equal')
axes[0].plot(kut1, domet1, 'b')                                  #type: ignore
axes[0].plot(kut1, vrijeme1, 'r')                                #type: ignore
axes[0].set_xlabel('')                                           #type: ignore
axes[0].set_ylabel('')                                           #type: ignore
axes[0].xaxis.set_major_locator(tick.MultipleLocator(5))         #type: ignore
axes[0].yaxis.set_major_locator(tick.MultipleLocator(4))         #type: ignore
axes[0].set_title('Odnos dometa i vremena trajanja gibanja o početnom \n kutu otklona za odabranu brzinu')     #type: ignore
axes[0].grid(lw=0.5)                                             #type: ignore
axes[0].axis('tight')                                            #type: ignore
axes[0].legend(['domet   [$m$]', 'vrijeme   [$s$]'], loc='best') #type: ignore
axes[1].plot(kut2, domet2, 'b')                                  #type: ignore
axes[1].plot(kut2, vrijeme2, 'r')                                #type: ignore
axes[1].set_xlabel('')                                           #type: ignore
axes[1].set_ylabel('')                                           #type: ignore
axes[1].xaxis.set_major_locator(tick.MultipleLocator(5))         #type: ignore
axes[1].yaxis.set_major_locator(tick.MultipleLocator(4))         #type: ignore
axes[1].set_title('Odnos dometa i vremena trajanja gibanja o početnom \n kutu otklona za fiksnu brzinu')       #type: ignore
axes[1].grid(lw=0.5)                                             #type: ignore
axes[1].axis('tight')                                            #type: ignore
axes[1].legend(['domet   [$m$]', 'vrijeme   [$s$]'], loc='best') #type: ignore

plt.show()    

