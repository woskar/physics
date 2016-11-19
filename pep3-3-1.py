"""
# Zeige Plots direkt im Jupyter Notebook an
%matplotlib inline
# Anschließend können wir das Modul importieren
import matplotlib.pyplot as plt # Die Abkürzung `plt` ist Konvention
# Numpy brauchen wir immer.
import numpy as np
x = np.linspace(0, 2 * np.pi, 100)
# Plot mit Label für Legende
plt.plot(x, np.sin(x), label=r'$A \times \sin(\phi)$')
plt.plot(x, np.cos(x), label=r'$A \times \cos(\phi)$')
# Titel
plt.title('Oszillation')
# Achsenlimits
plt.xlim(0, 2 * np.pi)
plt.ylim(-1, 1)
# Achsenbeschriftungen
plt.xlabel(r'Winkel $\phi \, [\mathrm{rad}]$')
plt.ylabel(r'Auslenkung $d \, [\mathrm{cm}]$')
# Legende
plt.legend(loc='lower left')
"""

#%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

q = lambda x, Q, y, w: ((2*Q)/(((np.pi*2)**0.5)*(w-x)**2))*(y+1j*(w-x))
x = np.linspace(0, 70, 200)
plt.plot(x, q(x, 1, 3, 31.4))

#         (((2*1**2)/(2*np.pi))*(1/(3.0**2+(x-31.4)**2)) )   )
#plt.plot()
plt.title('PEP3 Blatt3 Aufgabe1: Fouriertransformierte')
#plt.xlabel('$\omega$')
#plt.ylabel('$\q(\omega)$')
