import matplotlib.pyplot as plt
import numpy as np
import math

#def funkcija(x):
    #return  3*(x**2)


def derivation(funkcija, x, e, metoda):
    '''
    Funkcija koja racuna vrijednost funkcije u točki x koju odabire korisnik. Korisnik
    bira diferencijal  e  te metodu derivacije koja može imati vrijednost 2 ili 3.
    '''
    if metoda == 2:
        deriv = (funkcija(x) - funkcija(x-e))/e
    elif metoda == 3:
        deriv = (funkcija(x+e) - funkcija(x-e))/(2*e)
    return deriv            #type: ignore

def derivation_range(funkcija, a, b, e, metoda):
    '''
    Funkcija koja racuna vrijednost funkcije u rasponu točaka od A do B koji odabire korisnik.
    Korisnik bira diferencijal  e  te metodu derivacije koja može imati vrijednost 2 ili 3.
    '''
    prije = np.arange(a, b+0.001, 0.001)
    poslije = []
    for i in range(len(prije)):
        if metoda == 2:
            poslije.append(derivation(funkcija, prije[i], e, 2))
        elif metoda == 3:
            poslije.append(derivation(funkcija, prije[i], e, 3))
    return prije, poslije

def integral_sqare(funkcija, a, b, br):
    '''
    Funkcija koja kao ulazne parametre prima funkciju, granice integracije i broj podjela
    za numeričku integraciju, a vraća gornju i donju među koristeći pravokutnu aproksimaciju.    
    '''
    e = (b-a)/br
    x = np.arange(a, b+0.0001, e)
    donja = 0
    gornja = 0
    for i in range(len(x)):
        gornja += funkcija(x[i])*e
        donja += funkcija(x[i-1])*e
    return gornja, donja

def integral_trapezoid(funkcija, a, b, br):
    e = (b-a)/br
    inter = 0
    x = np.arange(a, b+0.0001, e)
    for i in range(len(x)):
        inter += (funkcija(x[i-1]) + funkcija(x[i]))*(e/2)
    return inter

#print(derivation(funkcija, 3, 0.001, 2))
#print(derivation_range(funkcija, 1, 4, 0.001, 3)[0], derivation_range(funkcija, 1, 4, 0.001, 3)[1])
#print(integral_sqare(funkcija, 0, 3, 1000)) 
#print(integral_trapezoid(funkcija, 0, 3, 1000))   