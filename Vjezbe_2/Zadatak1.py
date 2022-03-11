import matplotlib.pyplot as plt



def gibanje():
    sila = float(input('Upiši vrijednost sile u N koja djeluje na tijelo: '))
    masa = float(input('Upiši masu tijela u kg na kojeg djeluje sila: '))
    akceleracija =[]
    vrijeme = []
    brzina = []
    put = []

    #v=a*t
    #x=0.5*a*t^2
    a = sila / masa
    dt = 0.001
    while dt <= 10:
        vrijeme.append(dt)
        dt += dt
    for i in range(len(vrijeme)):
        v = a*vrijeme[i]
        brzina.append(v)
        x = 0.5*a*(vrijeme[i])**2 
        put.append(x)
        A = (vrijeme[i]/vrijeme[i])*a
        akceleracija.append(A)
            
    fig, ((axes1, axes2), (axes3, axes4)) = plt.subplots(nrows=2, ncols=2, figsize=(6,4), dpi=250)
    plt.axis('equal')
    plt.rcParams.update({'font.size': 7})
    axes1.plot(vrijeme, akceleracija, 'b')
    axes1.set_xlabel('$t [s]$')
    axes1.set_ylabel('$a [m/s^2]$')
    axes1.set_title('(1) a-t dijagram')
    axes1.grid()
    axes2.plot(vrijeme, brzina, 'r')
    axes2.set_xlabel('$t [s]$')
    axes2.set_ylabel('$v [m/s]$')
    axes2.set_title('(2) v-t dijagram')
    axes2.grid()
    axes3.plot(vrijeme, put, 'g')
    axes3.set_xlabel('$t [s]$')
    axes3.set_ylabel('$x [m]$')
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



print(gibanje())  