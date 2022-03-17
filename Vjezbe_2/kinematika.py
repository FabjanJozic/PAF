import matplotlib.pyplot as plt  
import math 
import numpy as np 
import os 




def jednoliko_gibanje(F, m, t):
    akceleracija = [F/m]
    vrijeme = [0]
    brzina = [0]
    put = [0]
    #dv=a*dt
    #dx=v*dt
    dt = 0.001
    for i in range(1000*t):
        vrijeme.append(i*(dt))  # type: ignore
        brzina.append(brzina[i]+akceleracija[i]*(dt))
        put.append(put[i]+brzina[i]*(dt))     # type: ignore
        akceleracija.append(F/m)  
    fig, ((axes1, axes2), (axes3, axes4)) = plt.subplots(nrows=2, ncols=2, figsize=(9,5.5), dpi=150)  # type: ignore
    plt.axis('equal')
    plt.rcParams.update({'font.size': 7.5})  # type: ignore
    axes1.plot(vrijeme, akceleracija, 'b')
    axes1.set_xlabel('$t | [s]$')
    axes1.set_ylabel('$a | [m/s^2]$')
    axes1.set_title('(1) a-t dijagram')
    axes1.grid()
    axes2.plot(vrijeme, brzina, 'r')
    axes2.set_xlabel('$t | [s]$')
    axes2.set_ylabel('$v | [m/s]$')
    axes2.set_title('(2) v-t dijagram')
    axes2.grid()
    axes3.plot(vrijeme, put, 'g')
    axes3.set_xlabel('$t | [s]$')
    axes3.set_ylabel('$x | [m]$')
    axes3.set_title('(3) x-t dijagram')
    axes3.grid()
    axes4.plot(0, 0, 'w*')
    axes4.plot(1, 1, 'w*')
    axes4.plot(2, 2, 'w*')
    axes4.legend(['Dijagram (1) prikazuje ovisnost akceleracija o vremenu \nza tijelo određene mase na koje djeluje određena sila.\n', 
                 'Dijagram (2) prikazuje ovisnost brzine o vremenu za \ntijelo određene mase na koje djeluje određena sila.\n',
                 'Dijagram (3) prikazuje ovisnost prijeđenog puta o vremenu \nza tijelo određene mase na koje djeluje određena sila.\n'],
                 loc = 'center')
    fig.tight_layout()
    slika = plt.show()
    return slika


def kosi_hitac(v, kut, t):
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
    for i in range(1000*t):
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



