import matplotlib.pyplot as plt
import os
import numpy as np



def jednadzba_pravca():
    A1 = int(input('Upiši vrijednost x koordinate prve točke: '))
    A2 = int(input('Upiši vrijednost y koordinate prve točke: '))
    B1 = int(input('Upiši vrijednost x koordinate druge točke: '))
    B2 = int(input('Upiši vrijednost y koordinate druge točke: '))
    xkoordinate = [A1, B1]
    ykoordinate = [A2, B2]

    #y-y0=k(x-x0)
    k = (B2 - A2)/(B1 - A1)
    if A1 < B1:
        X = np.linspace(A1-2, B1+2, 1000)
    else:
        X = np.linspace(A1+2, B1-2, 1000)
    Y = k*(X - A1) + A2

    naslov = input('Kako želite da se zove naslov grafa? ')

    x = [i for i in xkoordinate]
    y = [e for e in ykoordinate]
    fig = plt.figure(figsize=(5,3), dpi=200)
    axes = fig.add_axes([0.2, 0.2, 0.6, 0.6])
    axes.plot(x, y, 'r*')
    axes.plot(X, Y, 'b')
    axes.set_xlabel('x-os')
    axes.set_ylabel('y-os')
    axes.set_title(naslov)
    
    n = ['A', 'B']
    for i, txt in enumerate(n):
        for u, v in zip(xkoordinate, ykoordinate):
            plt.text(u ,v ,'  ({}, {})'.format(u, v))
            plt.axis([min(x)-2.5, max(x)+2.5, min(y)-2, max(y)+2])
            axes.annotate(txt, (x[i], y[i])) 

    pitanje = input('Ako želite dobiti ispis grafa na ekranu upišite  E, a ako želite ispis u PDF dokumentu upišite  P. ')
    if pitanje == 'E':
        slika = plt.show()
    elif pitanje == 'P':
        slika = fig.savefig(os.path.join('Zadatak5.pdf'))
    else:
        print('Pogreška pri odabiru opcije ispisa grafa.')

    return slika



jednadzba_pravca()