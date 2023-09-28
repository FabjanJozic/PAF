import numpy as np  #kom
import matplotlib.pyplot as plt
import sys
import matplotlib.ticker as ticker


sys.getdefaultencoding()

nezavisne_varijable = [0.0016, 0.0036, 0.0064, 0.010, 0.0144, 0.0196, 0.0256, 0.0324, 0.04]
zavisne_varijable = [0.1839, 0.2590, 0.3534, 0.4594, 0.7206, 0.9626, 1.2544, 1.4695, 1.9105]

naziv_grafa = '$T^2 - d^2$ graf'

slobodni_clan = 0.133
koeficijent_smjera = 41.634

x = [i for i in np.arange(0.0, 0.05, 0.0001)]
y = [i*koeficijent_smjera+slobodni_clan for i in x]
    

fig = plt.figure(figsize=(16,7), dpi=70)
axes = fig.add_axes([0.15, 0.15, 0.75, 0.70])
plt.rcParams.update({'font.size': 8})           #type: ignore
axes.scatter(nezavisne_varijable, zavisne_varijable, color='magenta')
axes.plot(x, y, color='blue', lw=0.6)
axes.set_xlabel('kvadrirana udaljenost na letvi od njezinog cetra   $d^2 [m^2]$' )
axes.set_ylabel('kvadrirani period titranja   $T^2 [s^2]$' )
axes.grid(lw=0.5)
axes.set_title(naziv_grafa)
axes.legend(['izmjereni podaci', 'Fit'], loc='best')
axes.xaxis.set_major_locator(ticker.MultipleLocator(0.003))   #type: ignore
axes.yaxis.set_major_locator(ticker.MultipleLocator(0.2))   #type: ignore
formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True) 
formatter.set_powerlimits((-1,1)) 
axes.xaxis.set_major_formatter(formatter) 
plt.show()
