import matplotlib.pyplot as plt
import numpy as np



def graf_gibanje(F, m):
    akceleracija =[F/m]
    vrijeme = [0]
    brzina = [0]
    put = [0]

    #dv=a*dt
    #dx=v*dt
    dt = 0.001
    
    for i in range(10000):
        vrijeme.append(i*(dt))  # type: ignore
        brzina.append(brzina[i]+akceleracija[i]*(dt))
        put.append(put[i]+brzina[i]*(dt))     # type: ignore
        akceleracija.append(F/m)
        
    fig, ((axes1, axes2), (axes3, axes4)) = plt.subplots(nrows=2, ncols=2, figsize=(9,5.5), dpi=100)  # type: ignore
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




graf_gibanje(20, 12)