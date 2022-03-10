import numpy as np
import matplotlib.pyplot as plt


def gibanje():
    F = float(input('Upiši vrijednost sile u N koja djeluje na tijelo: '))
    m = float(input('Upiši masu tijela u kg na kojeg djeluje sila: '))

    a = F/m
    t = np.linspace(0, 10, 10000)
    x = []
    v = []
    x0 = 0
    v0 = 0
    for i in range(len(t)):
        v0 += a*t[i]
        v.append(v0)
    for e in range(len(v)):
        x0 += t*v[e]
        x.append(x0)

    fig, axes = plt.subplots(1, 3, figsize=(8, 6), dpi=250)
    axes = fig.add_axes()
    axes.set_aspect('equal')
    plt.axis('equal')
    axes[0].plot(a, t, 'b')
    axes[0].set_xlabel('$t [s]$')
    axes[0].set_ylabel('$a [m/s^2]$')
    axes[0].set_title('a-t dijagram')
    axes[0].grid()
    axes[1].plot(v, t, 'r')
    axes[1].set_xlabel('$t [s]$')
    axes[1].set_ylabel('$v [m/s]$')
    axes[1].set_title('v-t dijagram')
    axes[1].grid()
    axes[2].plot(x, t, 'g')
    axes[2].set_xlabel('$t [s]$')
    axes[2].set_ylabel('$x [m]$')
    axes[2].set_title('x-t dijagram')
    axes[2].grid()
    fig.tight_layout()
    slika = plt.show()
    
    return slika


print(gibanje())  