import matplotlib.pyplot as plt
import numpy as np




def kosi_hitac(v, kut):
    kut_rad = (kut / 180)*np.pi
    vrijeme = [0]
    xbrzina = [v*np.cos(kut_rad)]
    ybrzina = [v*np.sin(kut_rad)]
    xpomak = [0]
    ypomak = [0]
    g = 9.81
    
    #x(t)=v*cos(a)*t+x0
    #y(t)=-0.5*g*t^2+v*sin(a)*t+y0
    dt = 0.001
    for i in range(10000):
        vrijeme.append(i*(dt))  # type: ignore
        xbrzina.append(v*np.cos(kut_rad))
        ybrzina.append(ybrzina[i]-g*(dt))
        xpomak.append(xpomak[i]+xbrzina[i]*(dt))
        ypomak.append(ypomak[i]+ybrzina[i]*(dt))
        
    fig, ((axes1, axes2), (axes3, axes4)) = plt.subplots(nrows=2, ncols=2, figsize=(9,5.5), dpi=150)  # type: ignore
    plt.axis('equal')  # type: ignore
    plt.rcParams.update({'font.size': 9})  # type: ignore
    axes1.plot(xpomak, ypomak, 'k')
    axes1.set_xlabel('$x | [m]$')
    axes1.set_ylabel('$y | [m]$')
    axes1.set_title('(1) x-y dijagram')
    axes1.grid()
    axes2.plot(vrijeme, xpomak, 'r')
    axes2.set_xlabel('$t | [s]$')
    axes2.set_ylabel('$v | [m]$')
    axes2.set_title('(2) x-t dijagram')
    axes2.grid()
    axes3.plot(vrijeme, ypomak, 'b')
    axes3.set_xlabel('$t | [s]$')
    axes3.set_ylabel('$y | [m]$')
    axes3.set_title('(3) y-t dijagram')
    axes3.grid()
    axes4.plot(0, 0, 'w*')
    axes4.plot(1, 1, 'w*')
    axes4.plot(2, 2, 'w*')
    axes4.legend(['Dijagram (1) prikazuje ponašanje gibanja tijela \nu x i y osi u ravnini za vrijeme kosog hica.\n', 
                 'Dijagram (2) prikazuje ovisnost pomaka u x-osi \no vremenu za tijelo u kosom hicu.\n',
                 'Dijagram (3) prikazuje ovisnost pomaka u y-osi \no vremenu za tijelo u kosom hicu.\n'], loc = 'center')
    fig.tight_layout()
    slika = plt.show()  # type: ignore
    
    return slika
        


kosi_hitac(64, 79)