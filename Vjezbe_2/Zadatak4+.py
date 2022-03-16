import numpy as np
import matplotlib.pyplot as plt
import os
import math





def xy_graf(v, kut):
    '''
    Funkcija uzima vrijednost početne brzine i kuta u stupnjevima koji se preračunava
    u radijane, te vraća xy-graf gibanja tijela prilikom kosog hica. Funkcija prestaje
    crtati graf kada vrijednost y koordinate postane 0.
    '''
    kut_rad = (kut / 180)*np.pi
    xbrzina = [v*np.cos(kut_rad)]
    ybrzina = [v*np.sin(kut_rad)]
    g = 9.81
    dt = 0.001
    xpomak = [0]
    ypomak = [0.001]
    for i in range(20000000):
        if ypomak[i] >= 0:
            xbrzina.append(v*np.cos(kut_rad))
            ybrzina.append(ybrzina[i]-g*(dt))
            xpomak.append(xpomak[i]+xbrzina[i]*(dt))
            ypomak.append(ypomak[i]+ybrzina[i]*(dt))   
        else:
            break
    fig = plt.figure(figsize=(5,3), dpi=200)
    axes = fig.add_axes([0.2, 0.2, 0.7, 0.7])
    axes.plot(xpomak, ypomak, 'r')
    axes.set_xlabel('$x | [m]$')
    axes.set_ylabel('$y | [m]$')
    return plt.show()


def maksimalna_visina(v, kut, t):
    '''
    Funkcija uzima vrijednost početne brzine i kuta u stupnjevima koji se preračunava
    u radijane, te vraća maksimalnu visinu tijela prilikom njegovog gibanja u obliku
    kosog hica. Korisnik osim vrijednosti brzine i kuta također unosi iznos vremena u
    kojem se događalo gibanje.
    '''
    kut_rad = (kut / 180)*np.pi
    ybrzina = [v*np.sin(kut_rad)]
    g = 9.81
    dt = 0.001
    ypomak = [0]
    for i in range(int(1000*t)):
        ybrzina.append(ybrzina[i]-g*(dt))
        ypomak.append(ypomak[i]+ybrzina[i]*(dt))   
    ypomak.sort(reverse=True)
    visina = ypomak[0]
    return visina
            

def domet(v ,kut, t):
    '''
    Funkcija uzima vrijednost početne brzine i kuta u stupnjevima koji se preračunava
    u radijane, te vraća domet tijela prilikom njegovog gibanja u obliku kosog hica.
    Korisnik osim vrijednosti brzine i kuta također unosi iznos vremena u kojem se
    događalo gibanje.
    '''
    kut_rad = (kut / 180)*np.pi
    xbrzina = [v*np.cos(kut_rad)]
    dt = 0.001
    xpomak = [0]
    for i in range(int(1000*t)):
        xbrzina.append(v*np.cos(kut_rad))
        xpomak.append(xpomak[i]+xbrzina[i]*(dt))   
    xpomak.sort(reverse=True)
    domet = xpomak[0]
    return domet


def maksimalna_brzina(v, kut, t):
    '''
    Funkcija uzima vrijednost početne brzine i kuta u stupnjevima koji se preračunava
    u radijane, te vraća maksimalnu brzinu tijela prilikom njegovog gibanja u obliku
    kosog hica. Korisnik osim vrijednosti brzine i kuta također unosi iznos vremena u
    kojem se događalo gibanje.
    '''
    kut_rad = (kut / 180)*np.pi
    xbrzina = [v*np.cos(kut_rad)]
    ybrzina = [v*np.sin(kut_rad)]
    brzina = []
    g = 9.81
    dt = 0.001
    xpomak = [0]
    ypomak = [0]
    for i in range(int(1000*t)):
            xbrzina.append(v*np.cos(kut_rad))
            ybrzina.append(ybrzina[i]-g*(dt))
            xpomak.append(xpomak[i]+xbrzina[i]*(dt))
            ypomak.append(ypomak[i]+ybrzina[i]*(dt))
            brzina.append(math.sqrt((xbrzina[i])**2 + (ybrzina[i])**2))   
    brz = max(brzina)
    return brz


def meta(v, kut, Sx, Sy, r, t):
    '''
    Funkcija koja određuje položaj okrugle mete i računa je li tijelo ispaljeno pod nekim
    kutem pogodilo metu, a ako nije određuje najbližu udaljenost od mete. Funkcija također
    crta graf gdje je prikazan navedeni događaj.
    Korisnik upisuje podatke redom:
    - početna bzina u [m/s]
    - kut otklona od horizontale u stupnjevima pod kojim je tijelo ispaljeno
    - x koordinata središta mete
    - y koordinata središta mete
    - radijus mete u [m]
    - vrijeme promatranja u [s]
    '''
    kut_rad = (kut / 180)*np.pi
    xbrzina = [v*np.cos(kut_rad)]
    ybrzina = [v*np.sin(kut_rad)]
    xpomak = [0]
    ypomak = [0]
    udaljenost0 = []
    g = 9.81
    dt = 0.001
    for i in range(int(1000*t)):
        xbrzina.append(v*np.cos(kut_rad))
        ybrzina.append(ybrzina[i]-g*(dt))
        xpomak.append(xpomak[i]+xbrzina[i]*(dt))
        ypomak.append(ypomak[i]+ybrzina[i]*(dt))
        udaljenost0.append(math.sqrt((xpomak[i] - Sx)**2 + (ypomak[i] - Sy)**2) - r)
    udaljenost = min(udaljenost0)
    if udaljenost <= 0:
        opis = 'Tijelo je pogodilo metu.'
    else:
        opis = 'Tijelo je promašilo metu za {}m.'.format(udaljenost)
    fig = plt.figure(figsize=(6,4), dpi=200)
    axes = fig.add_axes([0.15, 0.15, 0.75, 0.75])
    axes.set_aspect('equal')
    plt.rcParams.update({'font.size': 8})           #type: ignore
    plt.axis('equal')
    axes.plot(0, 0, 'w*')
    axes.plot(xpomak, ypomak, 'r--')
    krug = plt.Circle((Sx, Sy), r, color = 'b')
    axes.add_patch(krug)
    axes.set_xlabel('x $[m]$')
    axes.set_ylabel('y $[m]$')
    axes.legend(['{}'.format(opis),'putanja tijela', 'meta'], loc = 'best')    
    axes.grid()
    return plt.show()

