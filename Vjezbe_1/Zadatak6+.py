import numpy as np 
import matplotlib.pyplot as plt
import os
import math



def kruznica():
    Ax = int(input('Upiši x koordinatu točke: '))
    Ay = int(input('Upiši y koordinatu točke: '))
    Sx = int(input('Upiši x koordinatu središta kružnice: '))
    Sy = int(input('Upiši y koordinatu središta kružnice: '))
    rad = float(input('Upiši vrijednost radijusa kružnice: '))

    #(x-x0)^2+(y-y0)^2=r^2
    if rad > 0:
        kut = np.linspace(0, 2*np.pi, 1000)
        x = rad * np.cos(kut) + Sx
        y = rad * np.sin(kut) + Sy
        udaljenost1 = math.sqrt((Ax - Sx)**2 + (Ay - Sy)**2)
        udaljenost2 = abs(udaljenost1 - rad)
    else:
        print('Pogreška pri upisu vrijednosti radijusa kružnice.')
    xkoordinate = [Ax, Sx]
    ykoordinate = [Ay, Sy]

    if udaljenost1 < rad:           #type: ignore
        opis = 'Točka A se nalazi unutar kružnice.'
    elif udaljenost1 == rad:        #type: ignore
        opis = 'Točka A se nalazi na kružnici.'
    else:
        opis = 'Točka A se nalazi izvan kružnice.'
    
    naslov = input('Upišite naziv prikaza: ')

    fig = plt.figure(figsize=(8,5), dpi=100)
    axes = fig.add_axes([0.15, 0.15, 0.75, 0.75])
    axes.set_aspect('equal')
    plt.rcParams.update({'font.size': 8})               #type: ignore
    plt.axis('equal')
    axes.plot(Ax, Ay, 'r*')
    axes.plot(Sx, Sy, 'b*')
    axes.plot(x, y, 'b')            #type: ignore
    axes.set_xlabel('x-os')
    axes.set_ylabel('y-os')
    axes.set_title(naslov)
    axes.legend(['{}'.format(opis)+'\n'+'Točka A udaljena je od kružnce za'+'\n'+'{}.'.format(udaljenost2), 'Središte kružnice točka S.', 'Kružnica.'], loc = 'best')       #type: ignore
    axes.grid()

    xxxx = [i for i in xkoordinate]
    yyyy = [j for j in ykoordinate]
    n = [' A', ' S']
    for i, txt in enumerate(n):
        for u, v in zip(xkoordinate, ykoordinate):
            plt.text(u ,v ,'   ({}, {})'.format(u, v))
            axes.annotate(txt, (xxxx[i], yyyy[i])) 

    pitanje = input('Ako želite dobiti ispis grafa na ekranu upišite  E, a ako želite ispis u PDF dokumentu upišite  P. ')
    if pitanje == 'E':
        slika = plt.show()
    elif pitanje == 'P':
        ime = input('Upišite ime pod kojim ćete ispis spremiti u dokument: ')
        slika = fig.savefig(os.path.join('{}.pdf'.format(ime)))
    else:
        print('Pogreška pri odabiru opcije ispisa grafa.')

    return slika            # type: ignore




kruznica()
