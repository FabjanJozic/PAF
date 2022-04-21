import matplotlib.pyplot as plt
import numpy as np
import math

#def funkcija(x):
    #return  3*(x**2)


def derivation(funkcija, x, e, metoda = 3):
    '''
    Funkcija koja racuna vrijednost derivacije funkcije u točki x koju odabire korisnik.
    Korisnik bira diferencijal  e  te metodu derivacije koja može imati vrijednost 2 ili 3.
    '''
    if metoda == 2:
        deriv = (funkcija(x) - funkcija(x-e))/e
    elif metoda == 3:
        deriv = (funkcija(x+e) - funkcija(x-e))/(2*e)
    return deriv            #type: ignore

def derivation_range(funkcija, a, b, e, metoda = 3):
    '''
    Funkcija koja racuna vrijednost derivacije funkcije u rasponu točaka od A do B koji odabire 
    korisnik. Korisnik bira diferencijal  e  te metodu derivacije koja može imati vrijednost 2 ili 3.
    '''
    prije = np.arange(a, b+0.001, 0.001)
    poslije = []
    for i in range(len(prije)):
        if metoda == 2:
            poslije.append(derivation(funkcija, prije[i], e, 2))
        elif metoda == 3:
            poslije.append(derivation(funkcija, prije[i], e, 3))
    return prije, poslije

def integral_square(funkcija, a, b, br):
    '''
    Funkcija koja kao ulazne parametre prima funkciju, granice integracije i broj podjela
    za numeričku integraciju, a vraća gornju i donju među koristeći pravokutnu aproksimaciju.    
    '''
    e = abs((b-a)/br)
    x = np.arange(a, b+0.0001, e)
    donja = 0
    gornja = 0
    integ = 0
    for i in range(len(x)):
        integ += funkcija(x[i])*e 
    gornja = integ - funkcija(a)*e
    donja = integ - funkcija(b)*e
    return gornja, donja

def integral_trapezoid(funkcija, a, b, br):
    '''
    Funkcija koja kao ulazne parametre prima funkciju, granice integracije i broj podjela
    za numeričku integraciju, a vraća vrijednost integrala koristeći trapeznu aproksimaciju. 
    '''
    e = abs((b-a)/br)
    trap = 0
    integ = 0
    x = np.arange(a, b+0.0001, e)
    for i in range(len(x)):
        integ += funkcija(x[i])*e
    trap = integ +(funkcija(a) + funkcija(b))*(e/2)
    return trap

#print(derivation(funkcija, 3, 0.001, 3))
#print(derivation_range(funkcija, 1, 4, 0.001, 2)[0], derivation_range(funkcija, 1, 4, 0.001, 2)[1])
#print(integral_square(funkcija, 0, 3, 1000)) 
#print(integral_trapezoid(funkcija, 0, 3, 1000))   